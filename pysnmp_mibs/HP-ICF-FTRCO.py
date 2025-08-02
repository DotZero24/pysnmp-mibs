_Y='hpFtrCoExpireBoot'
_X='hpFtrCoExpireDate'
_W='hpFtrCoExpireVidDelete'
_V='hpFtrCoExpireApplication'
_U='hpFtrCoExpireSlot'
_T='hpFtrCoRestrictVlans'
_S='hpFtrCoRestrictPorts'
_R='hpFtrCoRestrictMessage'
_Q='hpFtrCoRestrictStatus'
_P='hpFtrCoRestrictIdParm'
_O='hpFtrCoEntityStatus'
_N='hpFtrCoEntityDate'
_M='hpFtrCoRestrictNextIndex'
_L='hpFtrCoRestrictIndex'
_K='hpFtrCoRestrictId'
_J='TruthValue'
_I='SnmpAdminString'
_H='hpicfFtrCoGroup'
_G='not-accessible'
_F='IndexName'
_E='hpFtrCoEntityName'
_D='Integer32'
_C='read-create'
_B='HP-ICF-FTRCO'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
hpicfFtrCo=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,46))
if mibBuilder.loadTexts:hpicfFtrCo.setRevisions(('2010-06-01 00:00','2009-08-28 00:02'))
class VidList(TextualConvention,OctetString):status=_A;displayHint='512x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
class IndexName(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpicfFtrcoObjects_ObjectIdentity=ObjectIdentity
hpicfFtrcoObjects=_HpicfFtrcoObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,46,1))
_HpFtrCoEntityTable_Object=MibTable
hpFtrCoEntityTable=_HpFtrCoEntityTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,1))
if mibBuilder.loadTexts:hpFtrCoEntityTable.setStatus(_A)
_HpFtrCoEntityEntry_Object=MibTableRow
hpFtrCoEntityEntry=_HpFtrCoEntityEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,1,1))
hpFtrCoEntityEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpFtrCoEntityEntry.setStatus(_A)
class _HpFtrCoEntityName_Type(IndexName):subtypeSpec=IndexName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpFtrCoEntityName_Type.__name__=_F
_HpFtrCoEntityName_Object=MibTableColumn
hpFtrCoEntityName=_HpFtrCoEntityName_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,1,1,1),_HpFtrCoEntityName_Type())
hpFtrCoEntityName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpFtrCoEntityName.setStatus(_A)
class _HpFtrCoRestrictNextIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpFtrCoRestrictNextIndex_Type.__name__=_D
_HpFtrCoRestrictNextIndex_Object=MibTableColumn
hpFtrCoRestrictNextIndex=_HpFtrCoRestrictNextIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,1,1,2),_HpFtrCoRestrictNextIndex_Type())
hpFtrCoRestrictNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoRestrictNextIndex.setStatus(_A)
_HpFtrCoEntityDate_Type=DateAndTime
_HpFtrCoEntityDate_Object=MibTableColumn
hpFtrCoEntityDate=_HpFtrCoEntityDate_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,1,1,3),_HpFtrCoEntityDate_Type())
hpFtrCoEntityDate.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpFtrCoEntityDate.setStatus(_A)
_HpFtrCoEntityStatus_Type=RowStatus
_HpFtrCoEntityStatus_Object=MibTableColumn
hpFtrCoEntityStatus=_HpFtrCoEntityStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,1,1,4),_HpFtrCoEntityStatus_Type())
hpFtrCoEntityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoEntityStatus.setStatus(_A)
_HpFtrCoRestrictionTable_Object=MibTable
hpFtrCoRestrictionTable=_HpFtrCoRestrictionTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2))
if mibBuilder.loadTexts:hpFtrCoRestrictionTable.setStatus(_A)
_HpFtrCoRestrictEntry_Object=MibTableRow
hpFtrCoRestrictEntry=_HpFtrCoRestrictEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1))
hpFtrCoRestrictEntry.setIndexNames((0,_B,_E),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpFtrCoRestrictEntry.setStatus(_A)
class _HpFtrCoRestrictId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('vidIpConfig',1),('vidDelete',2),('portSecurity',3),('portAcl',4),('portSourcePortFilter',5),('portMeshing',6),('portLacp',7),('distributedTrunk',8),('portVirusThrottling',9),('portSflow',10),('portDhcpSnoop',11),('portLoopDetection',12),('portBpduPvstGuard',13),('qinq',14),('portQos',15),('portRateLimit',16),('portStaticMac',17),('portIpLockdown',18),('portIgmp',19),('portMirrorDestination',20),('portLinkConfig',21),('portLldp',22),('portKeepalive',23),('aclPermitLogging',24)))
_HpFtrCoRestrictId_Type.__name__=_D
_HpFtrCoRestrictId_Object=MibTableColumn
hpFtrCoRestrictId=_HpFtrCoRestrictId_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,1),_HpFtrCoRestrictId_Type())
hpFtrCoRestrictId.setMaxAccess(_G)
if mibBuilder.loadTexts:hpFtrCoRestrictId.setStatus(_A)
class _HpFtrCoRestrictIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpFtrCoRestrictIndex_Type.__name__=_D
_HpFtrCoRestrictIndex_Object=MibTableColumn
hpFtrCoRestrictIndex=_HpFtrCoRestrictIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,2),_HpFtrCoRestrictIndex_Type())
hpFtrCoRestrictIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpFtrCoRestrictIndex.setStatus(_A)
class _HpFtrCoRestrictIdParm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpFtrCoRestrictIdParm_Type.__name__=_D
_HpFtrCoRestrictIdParm_Object=MibTableColumn
hpFtrCoRestrictIdParm=_HpFtrCoRestrictIdParm_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,3),_HpFtrCoRestrictIdParm_Type())
hpFtrCoRestrictIdParm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoRestrictIdParm.setStatus(_A)
_HpFtrCoRestrictStatus_Type=RowStatus
_HpFtrCoRestrictStatus_Object=MibTableColumn
hpFtrCoRestrictStatus=_HpFtrCoRestrictStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,4),_HpFtrCoRestrictStatus_Type())
hpFtrCoRestrictStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoRestrictStatus.setStatus(_A)
class _HpFtrCoRestrictMessage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpFtrCoRestrictMessage_Type.__name__=_I
_HpFtrCoRestrictMessage_Object=MibTableColumn
hpFtrCoRestrictMessage=_HpFtrCoRestrictMessage_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,5),_HpFtrCoRestrictMessage_Type())
hpFtrCoRestrictMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoRestrictMessage.setStatus(_A)
_HpFtrCoRestrictPorts_Type=PortList
_HpFtrCoRestrictPorts_Object=MibTableColumn
hpFtrCoRestrictPorts=_HpFtrCoRestrictPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,6),_HpFtrCoRestrictPorts_Type())
hpFtrCoRestrictPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoRestrictPorts.setStatus(_A)
_HpFtrCoRestrictVlans_Type=VidList
_HpFtrCoRestrictVlans_Object=MibTableColumn
hpFtrCoRestrictVlans=_HpFtrCoRestrictVlans_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,7),_HpFtrCoRestrictVlans_Type())
hpFtrCoRestrictVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoRestrictVlans.setStatus(_A)
class _HpFtrCoExpireSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpFtrCoExpireSlot_Type.__name__=_D
_HpFtrCoExpireSlot_Object=MibTableColumn
hpFtrCoExpireSlot=_HpFtrCoExpireSlot_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,8),_HpFtrCoExpireSlot_Type())
hpFtrCoExpireSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoExpireSlot.setStatus(_A)
class _HpFtrCoExpireApplication_Type(IndexName):subtypeSpec=IndexName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpFtrCoExpireApplication_Type.__name__=_F
_HpFtrCoExpireApplication_Object=MibTableColumn
hpFtrCoExpireApplication=_HpFtrCoExpireApplication_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,9),_HpFtrCoExpireApplication_Type())
hpFtrCoExpireApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoExpireApplication.setStatus(_A)
class _HpFtrCoExpireVidDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_HpFtrCoExpireVidDelete_Type.__name__=_D
_HpFtrCoExpireVidDelete_Object=MibTableColumn
hpFtrCoExpireVidDelete=_HpFtrCoExpireVidDelete_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,10),_HpFtrCoExpireVidDelete_Type())
hpFtrCoExpireVidDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoExpireVidDelete.setStatus(_A)
_HpFtrCoExpireDate_Type=DateAndTime
_HpFtrCoExpireDate_Object=MibTableColumn
hpFtrCoExpireDate=_HpFtrCoExpireDate_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,11),_HpFtrCoExpireDate_Type())
hpFtrCoExpireDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoExpireDate.setStatus(_A)
class _HpFtrCoExpireBoot_Type(TruthValue):defaultValue=2
_HpFtrCoExpireBoot_Type.__name__=_J
_HpFtrCoExpireBoot_Object=MibTableColumn
hpFtrCoExpireBoot=_HpFtrCoExpireBoot_Object((1,3,6,1,4,1,11,2,14,11,5,1,46,1,2,1,12),_HpFtrCoExpireBoot_Type())
hpFtrCoExpireBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFtrCoExpireBoot.setStatus(_A)
_HpicfFtrCoConformance_ObjectIdentity=ObjectIdentity
hpicfFtrCoConformance=_HpicfFtrCoConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,46,2))
_HpicfFtrCoCompliances_ObjectIdentity=ObjectIdentity
hpicfFtrCoCompliances=_HpicfFtrCoCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,46,2,1))
_HpicfFtrCoGroups_ObjectIdentity=ObjectIdentity
hpicfFtrCoGroups=_HpicfFtrCoGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,46,2,2))
hpicfFtrCoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,46,2,2,1))
hpicfFtrCoGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpicfFtrCoGroup.setStatus(_A)
hpicfFtrCoCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,46,2,1,1))
hpicfFtrCoCompliance.setObjects(*((_B,_H),(_B,_H)))
if mibBuilder.loadTexts:hpicfFtrCoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VidList':VidList,_F:IndexName,'hpicfFtrCo':hpicfFtrCo,'hpicfFtrcoObjects':hpicfFtrcoObjects,'hpFtrCoEntityTable':hpFtrCoEntityTable,'hpFtrCoEntityEntry':hpFtrCoEntityEntry,_E:hpFtrCoEntityName,_M:hpFtrCoRestrictNextIndex,_N:hpFtrCoEntityDate,_O:hpFtrCoEntityStatus,'hpFtrCoRestrictionTable':hpFtrCoRestrictionTable,'hpFtrCoRestrictEntry':hpFtrCoRestrictEntry,_K:hpFtrCoRestrictId,_L:hpFtrCoRestrictIndex,_P:hpFtrCoRestrictIdParm,_Q:hpFtrCoRestrictStatus,_R:hpFtrCoRestrictMessage,_S:hpFtrCoRestrictPorts,_T:hpFtrCoRestrictVlans,_U:hpFtrCoExpireSlot,_V:hpFtrCoExpireApplication,_W:hpFtrCoExpireVidDelete,_X:hpFtrCoExpireDate,_Y:hpFtrCoExpireBoot,'hpicfFtrCoConformance':hpicfFtrCoConformance,'hpicfFtrCoCompliances':hpicfFtrCoCompliances,'hpicfFtrCoCompliance':hpicfFtrCoCompliance,'hpicfFtrCoGroups':hpicfFtrCoGroups,_H:hpicfFtrCoGroup})