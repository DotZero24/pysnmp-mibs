_Y='etsysMirrorConfigGroup2'
_X='etsysMirrorSystemGroup2'
_W='etsysMirrorConfigGroup'
_V='etsysMirrorSystemGroup'
_U='etsysMirrorDestinationControlMirrorFirstN'
_T='etsysMirrorDestinationNextAvailableIndex'
_S='etsysMirrorSystemMaxMirrorFirstN'
_R='ifIndex'
_Q='IF-MIB'
_P='etsysMirrorDestinationPortRowStatus'
_O='etsysMirrorDestinationPortStorageType'
_N='etsysMirrorDestinationControlRowStatus'
_M='etsysMirrorDestinationControlStorageType'
_L='etsysMirrorDestinationControlOwner'
_K='deprecated'
_J='etsysMirrorSystemMaxMirrorDestinationControlGroups'
_I='etsysMirrorSystemMaxLocalMirrorDestinationPorts'
_H='etsysMirrorSystemMaxRemoteMirrors'
_G='etsysMirrorSystemMaxLocalMirrors'
_F='etsysMirrorDestinationControlIndex'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='ENTERASYS-MIRROR-CONFIG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_Q,_R)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
etsysMirrorConfigMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,72))
if mibBuilder.loadTexts:etsysMirrorConfigMIB.setRevisions(('2012-08-22 12:16','2009-08-10 18:56'))
_EtsysMirrorSystem_ObjectIdentity=ObjectIdentity
etsysMirrorSystem=_EtsysMirrorSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,72,1))
_EtsysMirrorSystemMaxLocalMirrors_Type=Unsigned32
_EtsysMirrorSystemMaxLocalMirrors_Object=MibScalar
etsysMirrorSystemMaxLocalMirrors=_EtsysMirrorSystemMaxLocalMirrors_Object((1,3,6,1,4,1,5624,1,2,72,1,1),_EtsysMirrorSystemMaxLocalMirrors_Type())
etsysMirrorSystemMaxLocalMirrors.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMirrorSystemMaxLocalMirrors.setStatus(_B)
_EtsysMirrorSystemMaxRemoteMirrors_Type=Unsigned32
_EtsysMirrorSystemMaxRemoteMirrors_Object=MibScalar
etsysMirrorSystemMaxRemoteMirrors=_EtsysMirrorSystemMaxRemoteMirrors_Object((1,3,6,1,4,1,5624,1,2,72,1,2),_EtsysMirrorSystemMaxRemoteMirrors_Type())
etsysMirrorSystemMaxRemoteMirrors.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMirrorSystemMaxRemoteMirrors.setStatus(_B)
_EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Type=Unsigned32
_EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Object=MibScalar
etsysMirrorSystemMaxLocalMirrorDestinationPorts=_EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Object((1,3,6,1,4,1,5624,1,2,72,1,3),_EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Type())
etsysMirrorSystemMaxLocalMirrorDestinationPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMirrorSystemMaxLocalMirrorDestinationPorts.setStatus(_B)
_EtsysMirrorSystemMaxMirrorDestinationControlGroups_Type=Unsigned32
_EtsysMirrorSystemMaxMirrorDestinationControlGroups_Object=MibScalar
etsysMirrorSystemMaxMirrorDestinationControlGroups=_EtsysMirrorSystemMaxMirrorDestinationControlGroups_Object((1,3,6,1,4,1,5624,1,2,72,1,4),_EtsysMirrorSystemMaxMirrorDestinationControlGroups_Type())
etsysMirrorSystemMaxMirrorDestinationControlGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMirrorSystemMaxMirrorDestinationControlGroups.setStatus(_B)
_EtsysMirrorSystemMaxMirrorFirstN_Type=Unsigned32
_EtsysMirrorSystemMaxMirrorFirstN_Object=MibScalar
etsysMirrorSystemMaxMirrorFirstN=_EtsysMirrorSystemMaxMirrorFirstN_Object((1,3,6,1,4,1,5624,1,2,72,1,5),_EtsysMirrorSystemMaxMirrorFirstN_Type())
etsysMirrorSystemMaxMirrorFirstN.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMirrorSystemMaxMirrorFirstN.setStatus(_B)
_EtsysMirrorConfig_ObjectIdentity=ObjectIdentity
etsysMirrorConfig=_EtsysMirrorConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,72,2))
class _EtsysMirrorDestinationNextAvailableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_EtsysMirrorDestinationNextAvailableIndex_Type.__name__=_E
_EtsysMirrorDestinationNextAvailableIndex_Object=MibScalar
etsysMirrorDestinationNextAvailableIndex=_EtsysMirrorDestinationNextAvailableIndex_Object((1,3,6,1,4,1,5624,1,2,72,2,1),_EtsysMirrorDestinationNextAvailableIndex_Type())
etsysMirrorDestinationNextAvailableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMirrorDestinationNextAvailableIndex.setStatus(_B)
_EtsysMirrorDestinationControlTable_Object=MibTable
etsysMirrorDestinationControlTable=_EtsysMirrorDestinationControlTable_Object((1,3,6,1,4,1,5624,1,2,72,2,2))
if mibBuilder.loadTexts:etsysMirrorDestinationControlTable.setStatus(_B)
_EtsysMirrorDestinationControlEntry_Object=MibTableRow
etsysMirrorDestinationControlEntry=_EtsysMirrorDestinationControlEntry_Object((1,3,6,1,4,1,5624,1,2,72,2,2,1))
etsysMirrorDestinationControlEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:etsysMirrorDestinationControlEntry.setStatus(_B)
_EtsysMirrorDestinationControlIndex_Type=Unsigned32
_EtsysMirrorDestinationControlIndex_Object=MibTableColumn
etsysMirrorDestinationControlIndex=_EtsysMirrorDestinationControlIndex_Object((1,3,6,1,4,1,5624,1,2,72,2,2,1,1),_EtsysMirrorDestinationControlIndex_Type())
etsysMirrorDestinationControlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysMirrorDestinationControlIndex.setStatus(_B)
_EtsysMirrorDestinationControlOwner_Type=SnmpAdminString
_EtsysMirrorDestinationControlOwner_Object=MibTableColumn
etsysMirrorDestinationControlOwner=_EtsysMirrorDestinationControlOwner_Object((1,3,6,1,4,1,5624,1,2,72,2,2,1,2),_EtsysMirrorDestinationControlOwner_Type())
etsysMirrorDestinationControlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMirrorDestinationControlOwner.setStatus(_B)
_EtsysMirrorDestinationControlStorageType_Type=StorageType
_EtsysMirrorDestinationControlStorageType_Object=MibTableColumn
etsysMirrorDestinationControlStorageType=_EtsysMirrorDestinationControlStorageType_Object((1,3,6,1,4,1,5624,1,2,72,2,2,1,3),_EtsysMirrorDestinationControlStorageType_Type())
etsysMirrorDestinationControlStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMirrorDestinationControlStorageType.setStatus(_B)
_EtsysMirrorDestinationControlRowStatus_Type=RowStatus
_EtsysMirrorDestinationControlRowStatus_Object=MibTableColumn
etsysMirrorDestinationControlRowStatus=_EtsysMirrorDestinationControlRowStatus_Object((1,3,6,1,4,1,5624,1,2,72,2,2,1,4),_EtsysMirrorDestinationControlRowStatus_Type())
etsysMirrorDestinationControlRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMirrorDestinationControlRowStatus.setStatus(_B)
class _EtsysMirrorDestinationControlMirrorFirstN_Type(Unsigned32):defaultValue=0
_EtsysMirrorDestinationControlMirrorFirstN_Type.__name__=_E
_EtsysMirrorDestinationControlMirrorFirstN_Object=MibTableColumn
etsysMirrorDestinationControlMirrorFirstN=_EtsysMirrorDestinationControlMirrorFirstN_Object((1,3,6,1,4,1,5624,1,2,72,2,2,1,5),_EtsysMirrorDestinationControlMirrorFirstN_Type())
etsysMirrorDestinationControlMirrorFirstN.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMirrorDestinationControlMirrorFirstN.setStatus(_B)
_EtsysMirrorDestinationPortTable_Object=MibTable
etsysMirrorDestinationPortTable=_EtsysMirrorDestinationPortTable_Object((1,3,6,1,4,1,5624,1,2,72,2,3))
if mibBuilder.loadTexts:etsysMirrorDestinationPortTable.setStatus(_B)
_EtsysMirrorDestinationPortEntry_Object=MibTableRow
etsysMirrorDestinationPortEntry=_EtsysMirrorDestinationPortEntry_Object((1,3,6,1,4,1,5624,1,2,72,2,3,1))
etsysMirrorDestinationPortEntry.setIndexNames((0,_A,_F),(0,_Q,_R))
if mibBuilder.loadTexts:etsysMirrorDestinationPortEntry.setStatus(_B)
_EtsysMirrorDestinationPortStorageType_Type=StorageType
_EtsysMirrorDestinationPortStorageType_Object=MibTableColumn
etsysMirrorDestinationPortStorageType=_EtsysMirrorDestinationPortStorageType_Object((1,3,6,1,4,1,5624,1,2,72,2,3,1,1),_EtsysMirrorDestinationPortStorageType_Type())
etsysMirrorDestinationPortStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMirrorDestinationPortStorageType.setStatus(_B)
_EtsysMirrorDestinationPortRowStatus_Type=RowStatus
_EtsysMirrorDestinationPortRowStatus_Object=MibTableColumn
etsysMirrorDestinationPortRowStatus=_EtsysMirrorDestinationPortRowStatus_Object((1,3,6,1,4,1,5624,1,2,72,2,3,1,2),_EtsysMirrorDestinationPortRowStatus_Type())
etsysMirrorDestinationPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMirrorDestinationPortRowStatus.setStatus(_B)
_EtsysMirrorConformance_ObjectIdentity=ObjectIdentity
etsysMirrorConformance=_EtsysMirrorConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,72,3))
_EtsysMirrorGroups_ObjectIdentity=ObjectIdentity
etsysMirrorGroups=_EtsysMirrorGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,72,3,1))
_EtsysMirrorCompliances_ObjectIdentity=ObjectIdentity
etsysMirrorCompliances=_EtsysMirrorCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,72,3,2))
etsysMirrorSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,72,3,1,1))
etsysMirrorSystemGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:etsysMirrorSystemGroup.setStatus(_K)
etsysMirrorConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,72,3,1,2))
etsysMirrorConfigGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:etsysMirrorConfigGroup.setStatus(_K)
etsysMirrorSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,72,3,1,3))
etsysMirrorSystemGroup2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_S)))
if mibBuilder.loadTexts:etsysMirrorSystemGroup2.setStatus(_B)
etsysMirrorConfigGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,72,3,1,4))
etsysMirrorConfigGroup2.setObjects(*((_A,_T),(_A,_L),(_A,_M),(_A,_N),(_A,_U),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:etsysMirrorConfigGroup2.setStatus(_B)
etsysMirrorCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,72,3,2,1))
etsysMirrorCompliance.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:etsysMirrorCompliance.setStatus(_K)
etsysMirrorCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,72,3,2,2))
etsysMirrorCompliance2.setObjects(*((_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:etsysMirrorCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysMirrorConfigMIB':etsysMirrorConfigMIB,'etsysMirrorSystem':etsysMirrorSystem,_G:etsysMirrorSystemMaxLocalMirrors,_H:etsysMirrorSystemMaxRemoteMirrors,_I:etsysMirrorSystemMaxLocalMirrorDestinationPorts,_J:etsysMirrorSystemMaxMirrorDestinationControlGroups,_S:etsysMirrorSystemMaxMirrorFirstN,'etsysMirrorConfig':etsysMirrorConfig,_T:etsysMirrorDestinationNextAvailableIndex,'etsysMirrorDestinationControlTable':etsysMirrorDestinationControlTable,'etsysMirrorDestinationControlEntry':etsysMirrorDestinationControlEntry,_F:etsysMirrorDestinationControlIndex,_L:etsysMirrorDestinationControlOwner,_M:etsysMirrorDestinationControlStorageType,_N:etsysMirrorDestinationControlRowStatus,_U:etsysMirrorDestinationControlMirrorFirstN,'etsysMirrorDestinationPortTable':etsysMirrorDestinationPortTable,'etsysMirrorDestinationPortEntry':etsysMirrorDestinationPortEntry,_O:etsysMirrorDestinationPortStorageType,_P:etsysMirrorDestinationPortRowStatus,'etsysMirrorConformance':etsysMirrorConformance,'etsysMirrorGroups':etsysMirrorGroups,_V:etsysMirrorSystemGroup,_W:etsysMirrorConfigGroup,_X:etsysMirrorSystemGroup2,_Y:etsysMirrorConfigGroup2,'etsysMirrorCompliances':etsysMirrorCompliances,'etsysMirrorCompliance':etsysMirrorCompliance,'etsysMirrorCompliance2':etsysMirrorCompliance2})