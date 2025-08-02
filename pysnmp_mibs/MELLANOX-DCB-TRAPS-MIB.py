_N='mellanoxDCBPortPFCPeerState'
_M='mellanoxDCBPortPFCOperState'
_L='mellanoxDCBPortPFCAdminState'
_K='mellanoxPFCProtocolState'
_J='mellanoxDCBPortETSPeerState'
_I='mellanoxDCBPortETSOperState'
_H='mellanoxDCBPortETSAdminState'
_G='mellanoxETSProtocolState'
_F='read-write'
_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='MELLANOX-DCB-TRAPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
mellanoxDCBTraps,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxDCBTraps')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxDCBTrapsMib=ModuleIdentity((1,3,6,1,4,1,33049,8,1))
if mibBuilder.loadTexts:mellanoxDCBTrapsMib.setRevisions(('2017-07-25 00:00',))
class ProtocolStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MellanoxDCBTrapsMibNotifications_ObjectIdentity=ObjectIdentity
mellanoxDCBTrapsMibNotifications=_MellanoxDCBTrapsMibNotifications_ObjectIdentity((1,3,6,1,4,1,33049,8,1,0))
_MellanoxDCBTrapsMibObjects_ObjectIdentity=ObjectIdentity
mellanoxDCBTrapsMibObjects=_MellanoxDCBTrapsMibObjects_ObjectIdentity((1,3,6,1,4,1,33049,8,1,1))
_MellanoxETSProtocolState_Type=ProtocolStateType
_MellanoxETSProtocolState_Object=MibScalar
mellanoxETSProtocolState=_MellanoxETSProtocolState_Object((1,3,6,1,4,1,33049,8,1,1,1),_MellanoxETSProtocolState_Type())
mellanoxETSProtocolState.setMaxAccess(_F)
if mibBuilder.loadTexts:mellanoxETSProtocolState.setStatus(_A)
_MellanoxPFCProtocolState_Type=ProtocolStateType
_MellanoxPFCProtocolState_Object=MibScalar
mellanoxPFCProtocolState=_MellanoxPFCProtocolState_Object((1,3,6,1,4,1,33049,8,1,1,2),_MellanoxPFCProtocolState_Type())
mellanoxPFCProtocolState.setMaxAccess(_F)
if mibBuilder.loadTexts:mellanoxPFCProtocolState.setStatus(_A)
_MellanoxDCBPortTable_Object=MibTable
mellanoxDCBPortTable=_MellanoxDCBPortTable_Object((1,3,6,1,4,1,33049,8,1,1,3))
if mibBuilder.loadTexts:mellanoxDCBPortTable.setStatus(_A)
_MellanoxDCBPortStatusEntry_Object=MibTableRow
mellanoxDCBPortStatusEntry=_MellanoxDCBPortStatusEntry_Object((1,3,6,1,4,1,33049,8,1,1,3,1))
mellanoxDCBPortStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mellanoxDCBPortStatusEntry.setStatus(_A)
_MellanoxDCBPortETSAdminState_Type=ProtocolStateType
_MellanoxDCBPortETSAdminState_Object=MibTableColumn
mellanoxDCBPortETSAdminState=_MellanoxDCBPortETSAdminState_Object((1,3,6,1,4,1,33049,8,1,1,3,1,1),_MellanoxDCBPortETSAdminState_Type())
mellanoxDCBPortETSAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxDCBPortETSAdminState.setStatus(_A)
_MellanoxDCBPortETSOperState_Type=ProtocolStateType
_MellanoxDCBPortETSOperState_Object=MibTableColumn
mellanoxDCBPortETSOperState=_MellanoxDCBPortETSOperState_Object((1,3,6,1,4,1,33049,8,1,1,3,1,2),_MellanoxDCBPortETSOperState_Type())
mellanoxDCBPortETSOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxDCBPortETSOperState.setStatus(_A)
_MellanoxDCBPortETSPeerState_Type=ProtocolStateType
_MellanoxDCBPortETSPeerState_Object=MibTableColumn
mellanoxDCBPortETSPeerState=_MellanoxDCBPortETSPeerState_Object((1,3,6,1,4,1,33049,8,1,1,3,1,3),_MellanoxDCBPortETSPeerState_Type())
mellanoxDCBPortETSPeerState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxDCBPortETSPeerState.setStatus(_A)
_MellanoxDCBPortPFCAdminState_Type=ProtocolStateType
_MellanoxDCBPortPFCAdminState_Object=MibTableColumn
mellanoxDCBPortPFCAdminState=_MellanoxDCBPortPFCAdminState_Object((1,3,6,1,4,1,33049,8,1,1,3,1,4),_MellanoxDCBPortPFCAdminState_Type())
mellanoxDCBPortPFCAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxDCBPortPFCAdminState.setStatus(_A)
_MellanoxDCBPortPFCOperState_Type=ProtocolStateType
_MellanoxDCBPortPFCOperState_Object=MibTableColumn
mellanoxDCBPortPFCOperState=_MellanoxDCBPortPFCOperState_Object((1,3,6,1,4,1,33049,8,1,1,3,1,5),_MellanoxDCBPortPFCOperState_Type())
mellanoxDCBPortPFCOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxDCBPortPFCOperState.setStatus(_A)
_MellanoxDCBPortPFCPeerState_Type=ProtocolStateType
_MellanoxDCBPortPFCPeerState_Object=MibTableColumn
mellanoxDCBPortPFCPeerState=_MellanoxDCBPortPFCPeerState_Object((1,3,6,1,4,1,33049,8,1,1,3,1,6),_MellanoxDCBPortPFCPeerState_Type())
mellanoxDCBPortPFCPeerState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxDCBPortPFCPeerState.setStatus(_A)
mellanoxETSModuleStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,1))
mellanoxETSModuleStateTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:mellanoxETSModuleStateTrap.setStatus(_A)
mellanoxETSPortAdminStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,2))
mellanoxETSPortAdminStateTrap.setObjects(*((_C,_D),(_B,_H)))
if mibBuilder.loadTexts:mellanoxETSPortAdminStateTrap.setStatus(_A)
mellanoxETSPortOperStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,3))
mellanoxETSPortOperStateTrap.setObjects(*((_C,_D),(_B,_I)))
if mibBuilder.loadTexts:mellanoxETSPortOperStateTrap.setStatus(_A)
mellanoxETSPortPeerStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,4))
mellanoxETSPortPeerStateTrap.setObjects(*((_C,_D),(_B,_J)))
if mibBuilder.loadTexts:mellanoxETSPortPeerStateTrap.setStatus(_A)
mellanoxPFCModuleStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,5))
mellanoxPFCModuleStateTrap.setObjects((_B,_K))
if mibBuilder.loadTexts:mellanoxPFCModuleStateTrap.setStatus(_A)
mellanoxPFCPortAdminStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,6))
mellanoxPFCPortAdminStateTrap.setObjects(*((_C,_D),(_B,_L)))
if mibBuilder.loadTexts:mellanoxPFCPortAdminStateTrap.setStatus(_A)
mellanoxPFCPortOperStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,7))
mellanoxPFCPortOperStateTrap.setObjects(*((_C,_D),(_B,_M)))
if mibBuilder.loadTexts:mellanoxPFCPortOperStateTrap.setStatus(_A)
mellanoxPFCPortPeerStateTrap=NotificationType((1,3,6,1,4,1,33049,8,1,0,8))
mellanoxPFCPortPeerStateTrap.setObjects(*((_C,_D),(_B,_N)))
if mibBuilder.loadTexts:mellanoxPFCPortPeerStateTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ProtocolStateType':ProtocolStateType,'mellanoxDCBTrapsMib':mellanoxDCBTrapsMib,'mellanoxDCBTrapsMibNotifications':mellanoxDCBTrapsMibNotifications,'mellanoxETSModuleStateTrap':mellanoxETSModuleStateTrap,'mellanoxETSPortAdminStateTrap':mellanoxETSPortAdminStateTrap,'mellanoxETSPortOperStateTrap':mellanoxETSPortOperStateTrap,'mellanoxETSPortPeerStateTrap':mellanoxETSPortPeerStateTrap,'mellanoxPFCModuleStateTrap':mellanoxPFCModuleStateTrap,'mellanoxPFCPortAdminStateTrap':mellanoxPFCPortAdminStateTrap,'mellanoxPFCPortOperStateTrap':mellanoxPFCPortOperStateTrap,'mellanoxPFCPortPeerStateTrap':mellanoxPFCPortPeerStateTrap,'mellanoxDCBTrapsMibObjects':mellanoxDCBTrapsMibObjects,_G:mellanoxETSProtocolState,_K:mellanoxPFCProtocolState,'mellanoxDCBPortTable':mellanoxDCBPortTable,'mellanoxDCBPortStatusEntry':mellanoxDCBPortStatusEntry,_H:mellanoxDCBPortETSAdminState,_I:mellanoxDCBPortETSOperState,_J:mellanoxDCBPortETSPeerState,_L:mellanoxDCBPortPFCAdminState,_M:mellanoxDCBPortPFCOperState,_N:mellanoxDCBPortPFCPeerState})