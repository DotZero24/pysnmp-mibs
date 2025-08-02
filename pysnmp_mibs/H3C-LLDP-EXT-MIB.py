_R='h3clldpPortAgingStatus'
_Q='h3clldpPortValidationStatus'
_P='read-only'
_O='interfaceName'
_N='networkAddress'
_M='macAddress'
_L='portComponent'
_K='interfaceAlias'
_J='default'
_I='h3clldpNbIdentityPortNum'
_H='not-accessible'
_G='h3clldpPortConfigPortNum'
_F='OctetString'
_E='h3clldpPortStatusPortNum'
_D='Integer32'
_C='H3C-LLDP-EXT-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
LldpPortNumber,=mibBuilder.importSymbols('LLDP-MIB','LldpPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3clldp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,100))
if mibBuilder.loadTexts:h3clldp.setRevisions(('2015-09-01 00:00','2009-03-21 00:00'))
_H3clldpObjects_ObjectIdentity=ObjectIdentity
h3clldpObjects=_H3clldpObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,100,1))
_H3clldpConfiguration_ObjectIdentity=ObjectIdentity
h3clldpConfiguration=_H3clldpConfiguration_ObjectIdentity((1,3,6,1,4,1,2011,10,2,100,1,1))
_H3clldpAdminStatus_Type=TruthValue
_H3clldpAdminStatus_Object=MibScalar
h3clldpAdminStatus=_H3clldpAdminStatus_Object((1,3,6,1,4,1,2011,10,2,100,1,1,1),_H3clldpAdminStatus_Type())
h3clldpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpAdminStatus.setStatus(_A)
_H3clldpComplianceCDPStatus_Type=TruthValue
_H3clldpComplianceCDPStatus_Object=MibScalar
h3clldpComplianceCDPStatus=_H3clldpComplianceCDPStatus_Object((1,3,6,1,4,1,2011,10,2,100,1,1,2),_H3clldpComplianceCDPStatus_Type())
h3clldpComplianceCDPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpComplianceCDPStatus.setStatus(_A)
_H3clldpPortConfigTable_Object=MibTable
h3clldpPortConfigTable=_H3clldpPortConfigTable_Object((1,3,6,1,4,1,2011,10,2,100,1,1,3))
if mibBuilder.loadTexts:h3clldpPortConfigTable.setStatus(_A)
_H3clldpPortConfigEntry_Object=MibTableRow
h3clldpPortConfigEntry=_H3clldpPortConfigEntry_Object((1,3,6,1,4,1,2011,10,2,100,1,1,3,1))
h3clldpPortConfigEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:h3clldpPortConfigEntry.setStatus(_A)
_H3clldpPortConfigPortNum_Type=LldpPortNumber
_H3clldpPortConfigPortNum_Object=MibTableColumn
h3clldpPortConfigPortNum=_H3clldpPortConfigPortNum_Object((1,3,6,1,4,1,2011,10,2,100,1,1,3,1,1),_H3clldpPortConfigPortNum_Type())
h3clldpPortConfigPortNum.setMaxAccess(_H)
if mibBuilder.loadTexts:h3clldpPortConfigPortNum.setStatus(_A)
class _H3clldpPortConfigCDPComplianceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('txAndRx',1),('disabled',2)))
_H3clldpPortConfigCDPComplianceStatus_Type.__name__=_D
_H3clldpPortConfigCDPComplianceStatus_Object=MibTableColumn
h3clldpPortConfigCDPComplianceStatus=_H3clldpPortConfigCDPComplianceStatus_Object((1,3,6,1,4,1,2011,10,2,100,1,1,3,1,2),_H3clldpPortConfigCDPComplianceStatus_Type())
h3clldpPortConfigCDPComplianceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpPortConfigCDPComplianceStatus.setStatus(_A)
_H3clldpPortConfigValidationAction_Type=Integer32
_H3clldpPortConfigValidationAction_Object=MibTableColumn
h3clldpPortConfigValidationAction=_H3clldpPortConfigValidationAction_Object((1,3,6,1,4,1,2011,10,2,100,1,1,3,1,3),_H3clldpPortConfigValidationAction_Type())
h3clldpPortConfigValidationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpPortConfigValidationAction.setStatus(_A)
_H3clldpPortConfigAgingAction_Type=Integer32
_H3clldpPortConfigAgingAction_Object=MibTableColumn
h3clldpPortConfigAgingAction=_H3clldpPortConfigAgingAction_Object((1,3,6,1,4,1,2011,10,2,100,1,1,3,1,4),_H3clldpPortConfigAgingAction_Type())
h3clldpPortConfigAgingAction.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpPortConfigAgingAction.setStatus(_A)
_H3clldpNbIdentityTable_Object=MibTable
h3clldpNbIdentityTable=_H3clldpNbIdentityTable_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4))
if mibBuilder.loadTexts:h3clldpNbIdentityTable.setStatus(_A)
_H3clldpNbIdentityEntry_Object=MibTableRow
h3clldpNbIdentityEntry=_H3clldpNbIdentityEntry_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1))
h3clldpNbIdentityEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:h3clldpNbIdentityEntry.setStatus(_A)
_H3clldpNbIdentityPortNum_Type=LldpPortNumber
_H3clldpNbIdentityPortNum_Object=MibTableColumn
h3clldpNbIdentityPortNum=_H3clldpNbIdentityPortNum_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1,1),_H3clldpNbIdentityPortNum_Type())
h3clldpNbIdentityPortNum.setMaxAccess(_H)
if mibBuilder.loadTexts:h3clldpNbIdentityPortNum.setStatus(_A)
class _H3clldpNbIdentityChassisIDSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),('chassisComponent',1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),('local',7)))
_H3clldpNbIdentityChassisIDSubtype_Type.__name__=_D
_H3clldpNbIdentityChassisIDSubtype_Object=MibTableColumn
h3clldpNbIdentityChassisIDSubtype=_H3clldpNbIdentityChassisIDSubtype_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1,2),_H3clldpNbIdentityChassisIDSubtype_Type())
h3clldpNbIdentityChassisIDSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpNbIdentityChassisIDSubtype.setStatus(_A)
class _H3clldpNbIdentityChassisID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3clldpNbIdentityChassisID_Type.__name__=_F
_H3clldpNbIdentityChassisID_Object=MibTableColumn
h3clldpNbIdentityChassisID=_H3clldpNbIdentityChassisID_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1,3),_H3clldpNbIdentityChassisID_Type())
h3clldpNbIdentityChassisID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpNbIdentityChassisID.setStatus(_A)
class _H3clldpNbIdentityPortIDSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),('agentCircuitId',6),('local',7)))
_H3clldpNbIdentityPortIDSubtype_Type.__name__=_D
_H3clldpNbIdentityPortIDSubtype_Object=MibTableColumn
h3clldpNbIdentityPortIDSubtype=_H3clldpNbIdentityPortIDSubtype_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1,4),_H3clldpNbIdentityPortIDSubtype_Type())
h3clldpNbIdentityPortIDSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpNbIdentityPortIDSubtype.setStatus(_A)
class _H3clldpNbIdentityPortID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3clldpNbIdentityPortID_Type.__name__=_F
_H3clldpNbIdentityPortID_Object=MibTableColumn
h3clldpNbIdentityPortID=_H3clldpNbIdentityPortID_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1,5),_H3clldpNbIdentityPortID_Type())
h3clldpNbIdentityPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3clldpNbIdentityPortID.setStatus(_A)
_H3clldpNbIdentityRowStatus_Type=RowStatus
_H3clldpNbIdentityRowStatus_Object=MibTableColumn
h3clldpNbIdentityRowStatus=_H3clldpNbIdentityRowStatus_Object((1,3,6,1,4,1,2011,10,2,100,1,1,4,1,6),_H3clldpNbIdentityRowStatus_Type())
h3clldpNbIdentityRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3clldpNbIdentityRowStatus.setStatus(_A)
_H3clldpPortStatusTable_Object=MibTable
h3clldpPortStatusTable=_H3clldpPortStatusTable_Object((1,3,6,1,4,1,2011,10,2,100,1,1,5))
if mibBuilder.loadTexts:h3clldpPortStatusTable.setStatus(_A)
_H3clldpPortStatusEntry_Object=MibTableRow
h3clldpPortStatusEntry=_H3clldpPortStatusEntry_Object((1,3,6,1,4,1,2011,10,2,100,1,1,5,1))
h3clldpPortStatusEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3clldpPortStatusEntry.setStatus(_A)
_H3clldpPortStatusPortNum_Type=LldpPortNumber
_H3clldpPortStatusPortNum_Object=MibTableColumn
h3clldpPortStatusPortNum=_H3clldpPortStatusPortNum_Object((1,3,6,1,4,1,2011,10,2,100,1,1,5,1,1),_H3clldpPortStatusPortNum_Type())
h3clldpPortStatusPortNum.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3clldpPortStatusPortNum.setStatus(_A)
_H3clldpPortValidationStatus_Type=Integer32
_H3clldpPortValidationStatus_Object=MibTableColumn
h3clldpPortValidationStatus=_H3clldpPortValidationStatus_Object((1,3,6,1,4,1,2011,10,2,100,1,1,5,1,2),_H3clldpPortValidationStatus_Type())
h3clldpPortValidationStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:h3clldpPortValidationStatus.setStatus(_A)
_H3clldpPortAgingStatus_Type=Integer32
_H3clldpPortAgingStatus_Object=MibTableColumn
h3clldpPortAgingStatus=_H3clldpPortAgingStatus_Object((1,3,6,1,4,1,2011,10,2,100,1,1,5,1,3),_H3clldpPortAgingStatus_Type())
h3clldpPortAgingStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:h3clldpPortAgingStatus.setStatus(_A)
_H3clldpNotifications_ObjectIdentity=ObjectIdentity
h3clldpNotifications=_H3clldpNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,100,2))
_H3clldpPortStatusTrap_ObjectIdentity=ObjectIdentity
h3clldpPortStatusTrap=_H3clldpPortStatusTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,100,2,0))
h3clldpValidationStatusChange=NotificationType((1,3,6,1,4,1,2011,10,2,100,2,0,1))
h3clldpValidationStatusChange.setObjects(*((_C,_E),(_C,_Q)))
if mibBuilder.loadTexts:h3clldpValidationStatusChange.setStatus(_A)
h3clldpAgingStatusChange=NotificationType((1,3,6,1,4,1,2011,10,2,100,2,0,2))
h3clldpAgingStatusChange.setObjects(*((_C,_E),(_C,_R)))
if mibBuilder.loadTexts:h3clldpAgingStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3clldp':h3clldp,'h3clldpObjects':h3clldpObjects,'h3clldpConfiguration':h3clldpConfiguration,'h3clldpAdminStatus':h3clldpAdminStatus,'h3clldpComplianceCDPStatus':h3clldpComplianceCDPStatus,'h3clldpPortConfigTable':h3clldpPortConfigTable,'h3clldpPortConfigEntry':h3clldpPortConfigEntry,_G:h3clldpPortConfigPortNum,'h3clldpPortConfigCDPComplianceStatus':h3clldpPortConfigCDPComplianceStatus,'h3clldpPortConfigValidationAction':h3clldpPortConfigValidationAction,'h3clldpPortConfigAgingAction':h3clldpPortConfigAgingAction,'h3clldpNbIdentityTable':h3clldpNbIdentityTable,'h3clldpNbIdentityEntry':h3clldpNbIdentityEntry,_I:h3clldpNbIdentityPortNum,'h3clldpNbIdentityChassisIDSubtype':h3clldpNbIdentityChassisIDSubtype,'h3clldpNbIdentityChassisID':h3clldpNbIdentityChassisID,'h3clldpNbIdentityPortIDSubtype':h3clldpNbIdentityPortIDSubtype,'h3clldpNbIdentityPortID':h3clldpNbIdentityPortID,'h3clldpNbIdentityRowStatus':h3clldpNbIdentityRowStatus,'h3clldpPortStatusTable':h3clldpPortStatusTable,'h3clldpPortStatusEntry':h3clldpPortStatusEntry,_E:h3clldpPortStatusPortNum,_Q:h3clldpPortValidationStatus,_R:h3clldpPortAgingStatus,'h3clldpNotifications':h3clldpNotifications,'h3clldpPortStatusTrap':h3clldpPortStatusTrap,'h3clldpValidationStatusChange':h3clldpValidationStatusChange,'h3clldpAgingStatusChange':h3clldpAgingStatusChange})