_Q='alAlarmFallingTrap'
_P='alAlarmRisingTrap'
_O='alTrapCounter'
_N='alTcaId'
_M='alSourceId'
_L='alCardId'
_K='alAlarmType'
_J='alDeviceIp'
_I='Integer32'
_H='alIndex'
_G='alTimestamp'
_F='alDescription'
_E='alSeverity'
_D='read-only'
_C='not-accessible'
_B='current'
_A='ALLOT-NX-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alRegMIB,=mibBuilder.importSymbols('ALLOT-MIB','alRegMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alNXMIB=ModuleIdentity((1,3,6,1,4,1,2603,10))
if mibBuilder.loadTexts:alNXMIB.setRevisions(('2008-12-10 10:00',))
_AlEvents_ObjectIdentity=ObjectIdentity
alEvents=_AlEvents_ObjectIdentity((1,3,6,1,4,1,2603,10,0))
_AlObjects_ObjectIdentity=ObjectIdentity
alObjects=_AlObjects_ObjectIdentity((1,3,6,1,4,1,2603,10,2))
_AlAlarmTable_Object=MibTable
alAlarmTable=_AlAlarmTable_Object((1,3,6,1,4,1,2603,10,2,1))
if mibBuilder.loadTexts:alAlarmTable.setStatus(_B)
_AlEntry_Object=MibTableRow
alEntry=_AlEntry_Object((1,3,6,1,4,1,2603,10,2,1,1))
alEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:alEntry.setStatus(_B)
_AlDeviceIp_Type=IpAddress
_AlDeviceIp_Object=MibTableColumn
alDeviceIp=_AlDeviceIp_Object((1,3,6,1,4,1,2603,10,2,1,1,1),_AlDeviceIp_Type())
alDeviceIp.setMaxAccess(_C)
if mibBuilder.loadTexts:alDeviceIp.setStatus(_B)
_AlAlarmType_Type=Unsigned32
_AlAlarmType_Object=MibTableColumn
alAlarmType=_AlAlarmType_Object((1,3,6,1,4,1,2603,10,2,1,1,2),_AlAlarmType_Type())
alAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:alAlarmType.setStatus(_B)
_AlCardId_Type=Unsigned32
_AlCardId_Object=MibTableColumn
alCardId=_AlCardId_Object((1,3,6,1,4,1,2603,10,2,1,1,3),_AlCardId_Type())
alCardId.setMaxAccess(_C)
if mibBuilder.loadTexts:alCardId.setStatus(_B)
_AlSourceId_Type=Unsigned32
_AlSourceId_Object=MibTableColumn
alSourceId=_AlSourceId_Object((1,3,6,1,4,1,2603,10,2,1,1,4),_AlSourceId_Type())
alSourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:alSourceId.setStatus(_B)
_AlTcaId_Type=Unsigned32
_AlTcaId_Object=MibTableColumn
alTcaId=_AlTcaId_Object((1,3,6,1,4,1,2603,10,2,1,1,5),_AlTcaId_Type())
alTcaId.setMaxAccess(_C)
if mibBuilder.loadTexts:alTcaId.setStatus(_B)
class _AlSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',0),('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6)))
_AlSeverity_Type.__name__=_I
_AlSeverity_Object=MibTableColumn
alSeverity=_AlSeverity_Object((1,3,6,1,4,1,2603,10,2,1,1,6),_AlSeverity_Type())
alSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:alSeverity.setStatus(_B)
_AlDescription_Type=OctetString
_AlDescription_Object=MibTableColumn
alDescription=_AlDescription_Object((1,3,6,1,4,1,2603,10,2,1,1,7),_AlDescription_Type())
alDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:alDescription.setStatus(_B)
_AlTimestamp_Type=Counter64
_AlTimestamp_Object=MibTableColumn
alTimestamp=_AlTimestamp_Object((1,3,6,1,4,1,2603,10,2,1,1,8),_AlTimestamp_Type())
alTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:alTimestamp.setStatus(_B)
_AlIndex_Type=OctetString
_AlIndex_Object=MibTableColumn
alIndex=_AlIndex_Object((1,3,6,1,4,1,2603,10,2,1,1,9),_AlIndex_Type())
alIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alIndex.setStatus(_B)
_AlTrapCounter_Type=Counter32
_AlTrapCounter_Object=MibScalar
alTrapCounter=_AlTrapCounter_Object((1,3,6,1,4,1,2603,10,2,2),_AlTrapCounter_Type())
alTrapCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:alTrapCounter.setStatus(_B)
_AlConf_ObjectIdentity=ObjectIdentity
alConf=_AlConf_ObjectIdentity((1,3,6,1,4,1,2603,10,3))
_AlGroups_ObjectIdentity=ObjectIdentity
alGroups=_AlGroups_ObjectIdentity((1,3,6,1,4,1,2603,10,3,1))
_AlCompls_ObjectIdentity=ObjectIdentity
alCompls=_AlCompls_ObjectIdentity((1,3,6,1,4,1,2603,10,3,2))
alBasicGroup=ObjectGroup((1,3,6,1,4,1,2603,10,3,1,1))
alBasicGroup.setObjects(*((_A,_E),(_A,_F),(_A,_O),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:alBasicGroup.setStatus(_B)
alAlarmRisingTrap=NotificationType((1,3,6,1,4,1,2603,10,0,1))
alAlarmRisingTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:alAlarmRisingTrap.setStatus(_B)
alAlarmFallingTrap=NotificationType((1,3,6,1,4,1,2603,10,0,2))
alAlarmFallingTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:alAlarmFallingTrap.setStatus(_B)
alBasicEvents=NotificationGroup((1,3,6,1,4,1,2603,10,3,1,2))
alBasicEvents.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:alBasicEvents.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alNXMIB':alNXMIB,'alEvents':alEvents,_P:alAlarmRisingTrap,_Q:alAlarmFallingTrap,'alObjects':alObjects,'alAlarmTable':alAlarmTable,'alEntry':alEntry,_J:alDeviceIp,_K:alAlarmType,_L:alCardId,_M:alSourceId,_N:alTcaId,_E:alSeverity,_F:alDescription,_G:alTimestamp,_H:alIndex,_O:alTrapCounter,'alConf':alConf,'alGroups':alGroups,'alBasicGroup':alBasicGroup,'alBasicEvents':alBasicEvents,'alCompls':alCompls})