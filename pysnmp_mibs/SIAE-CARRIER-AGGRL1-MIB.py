_G='carrierAggrActuatorIndex'
_F='carrierAggrSensorIndex'
_E='SIAE-CARRIER-AGGRL1-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
carrierAggr=ModuleIdentity((1,3,6,1,4,1,3373,1103,104))
if mibBuilder.loadTexts:carrierAggr.setRevisions(('2016-08-23 00:00',))
_CarrierAggrMibVersion_Type=Integer32
_CarrierAggrMibVersion_Object=MibScalar
carrierAggrMibVersion=_CarrierAggrMibVersion_Object((1,3,6,1,4,1,3373,1103,104,1),_CarrierAggrMibVersion_Type())
carrierAggrMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierAggrMibVersion.setStatus(_A)
_CarrierAggrSensorTable_Object=MibTable
carrierAggrSensorTable=_CarrierAggrSensorTable_Object((1,3,6,1,4,1,3373,1103,104,2))
if mibBuilder.loadTexts:carrierAggrSensorTable.setStatus(_A)
_CarrierAggrSensorEntry_Object=MibTableRow
carrierAggrSensorEntry=_CarrierAggrSensorEntry_Object((1,3,6,1,4,1,3373,1103,104,2,1))
carrierAggrSensorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:carrierAggrSensorEntry.setStatus(_A)
class _CarrierAggrSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CarrierAggrSensorIndex_Type.__name__=_C
_CarrierAggrSensorIndex_Object=MibTableColumn
carrierAggrSensorIndex=_CarrierAggrSensorIndex_Object((1,3,6,1,4,1,3373,1103,104,2,1,1),_CarrierAggrSensorIndex_Type())
carrierAggrSensorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierAggrSensorIndex.setStatus(_A)
_CarrierAggrSensorRowstatus_Type=RowStatus
_CarrierAggrSensorRowstatus_Object=MibTableColumn
carrierAggrSensorRowstatus=_CarrierAggrSensorRowstatus_Object((1,3,6,1,4,1,3373,1103,104,2,1,2),_CarrierAggrSensorRowstatus_Type())
carrierAggrSensorRowstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrSensorRowstatus.setStatus(_A)
class _CarrierAggrSensorAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_CarrierAggrSensorAdminStatus_Type.__name__=_C
_CarrierAggrSensorAdminStatus_Object=MibTableColumn
carrierAggrSensorAdminStatus=_CarrierAggrSensorAdminStatus_Object((1,3,6,1,4,1,3373,1103,104,2,1,3),_CarrierAggrSensorAdminStatus_Type())
carrierAggrSensorAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrSensorAdminStatus.setStatus(_A)
_CarrierAggrSensorIfIndex_Type=InterfaceIndexOrZero
_CarrierAggrSensorIfIndex_Object=MibTableColumn
carrierAggrSensorIfIndex=_CarrierAggrSensorIfIndex_Object((1,3,6,1,4,1,3373,1103,104,2,1,4),_CarrierAggrSensorIfIndex_Type())
carrierAggrSensorIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrSensorIfIndex.setStatus(_A)
class _CarrierAggrSensorHitlessCapability_Type(Bits):namedValues=NamedValues(('hitlessAvailable',0))
_CarrierAggrSensorHitlessCapability_Type.__name__='Bits'
_CarrierAggrSensorHitlessCapability_Object=MibTableColumn
carrierAggrSensorHitlessCapability=_CarrierAggrSensorHitlessCapability_Object((1,3,6,1,4,1,3373,1103,104,2,1,5),_CarrierAggrSensorHitlessCapability_Type())
carrierAggrSensorHitlessCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierAggrSensorHitlessCapability.setStatus(_A)
class _CarrierAggrSensorHitlessBehaviour_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_CarrierAggrSensorHitlessBehaviour_Type.__name__=_C
_CarrierAggrSensorHitlessBehaviour_Object=MibTableColumn
carrierAggrSensorHitlessBehaviour=_CarrierAggrSensorHitlessBehaviour_Object((1,3,6,1,4,1,3373,1103,104,2,1,6),_CarrierAggrSensorHitlessBehaviour_Type())
carrierAggrSensorHitlessBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrSensorHitlessBehaviour.setStatus(_A)
class _CarrierAggrSensorHitlessMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_CarrierAggrSensorHitlessMode_Type.__name__=_C
_CarrierAggrSensorHitlessMode_Object=MibTableColumn
carrierAggrSensorHitlessMode=_CarrierAggrSensorHitlessMode_Object((1,3,6,1,4,1,3373,1103,104,2,1,7),_CarrierAggrSensorHitlessMode_Type())
carrierAggrSensorHitlessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrSensorHitlessMode.setStatus(_A)
class _CarrierAggrSensorHitlessProfile_Type(Integer32):defaultValue=1
_CarrierAggrSensorHitlessProfile_Type.__name__=_C
_CarrierAggrSensorHitlessProfile_Object=MibTableColumn
carrierAggrSensorHitlessProfile=_CarrierAggrSensorHitlessProfile_Object((1,3,6,1,4,1,3373,1103,104,2,1,8),_CarrierAggrSensorHitlessProfile_Type())
carrierAggrSensorHitlessProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrSensorHitlessProfile.setStatus(_A)
class _CarrierAggrSensorHitlessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('goodZone',1),('hitlessZone',2),('badZone',3)))
_CarrierAggrSensorHitlessStatus_Type.__name__=_C
_CarrierAggrSensorHitlessStatus_Object=MibTableColumn
carrierAggrSensorHitlessStatus=_CarrierAggrSensorHitlessStatus_Object((1,3,6,1,4,1,3373,1103,104,2,1,9),_CarrierAggrSensorHitlessStatus_Type())
carrierAggrSensorHitlessStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierAggrSensorHitlessStatus.setStatus(_A)
_CarrierAggrActuatorTable_Object=MibTable
carrierAggrActuatorTable=_CarrierAggrActuatorTable_Object((1,3,6,1,4,1,3373,1103,104,3))
if mibBuilder.loadTexts:carrierAggrActuatorTable.setStatus(_A)
_CarrierAggrActuatorEntry_Object=MibTableRow
carrierAggrActuatorEntry=_CarrierAggrActuatorEntry_Object((1,3,6,1,4,1,3373,1103,104,3,1))
carrierAggrActuatorEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:carrierAggrActuatorEntry.setStatus(_A)
class _CarrierAggrActuatorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CarrierAggrActuatorIndex_Type.__name__=_C
_CarrierAggrActuatorIndex_Object=MibTableColumn
carrierAggrActuatorIndex=_CarrierAggrActuatorIndex_Object((1,3,6,1,4,1,3373,1103,104,3,1,1),_CarrierAggrActuatorIndex_Type())
carrierAggrActuatorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierAggrActuatorIndex.setStatus(_A)
_CarrierAggrActuatorRowStatus_Type=RowStatus
_CarrierAggrActuatorRowStatus_Object=MibTableColumn
carrierAggrActuatorRowStatus=_CarrierAggrActuatorRowStatus_Object((1,3,6,1,4,1,3373,1103,104,3,1,2),_CarrierAggrActuatorRowStatus_Type())
carrierAggrActuatorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrActuatorRowStatus.setStatus(_A)
class _CarrierAggrActuatorAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_CarrierAggrActuatorAdminStatus_Type.__name__=_C
_CarrierAggrActuatorAdminStatus_Object=MibTableColumn
carrierAggrActuatorAdminStatus=_CarrierAggrActuatorAdminStatus_Object((1,3,6,1,4,1,3373,1103,104,3,1,3),_CarrierAggrActuatorAdminStatus_Type())
carrierAggrActuatorAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrActuatorAdminStatus.setStatus(_A)
_CarrierAggrActuatorIfIndex_Type=InterfaceIndexOrZero
_CarrierAggrActuatorIfIndex_Object=MibTableColumn
carrierAggrActuatorIfIndex=_CarrierAggrActuatorIfIndex_Object((1,3,6,1,4,1,3373,1103,104,3,1,4),_CarrierAggrActuatorIfIndex_Type())
carrierAggrActuatorIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrActuatorIfIndex.setStatus(_A)
_CarrierAggrActuatorSensorIndex_Type=Integer32
_CarrierAggrActuatorSensorIndex_Object=MibTableColumn
carrierAggrActuatorSensorIndex=_CarrierAggrActuatorSensorIndex_Object((1,3,6,1,4,1,3373,1103,104,3,1,5),_CarrierAggrActuatorSensorIndex_Type())
carrierAggrActuatorSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:carrierAggrActuatorSensorIndex.setStatus(_A)
_CarrierAggrActuatorConcIpAddr_Type=IpAddress
_CarrierAggrActuatorConcIpAddr_Object=MibTableColumn
carrierAggrActuatorConcIpAddr=_CarrierAggrActuatorConcIpAddr_Object((1,3,6,1,4,1,3373,1103,104,3,1,6),_CarrierAggrActuatorConcIpAddr_Type())
carrierAggrActuatorConcIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierAggrActuatorConcIpAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'carrierAggr':carrierAggr,'carrierAggrMibVersion':carrierAggrMibVersion,'carrierAggrSensorTable':carrierAggrSensorTable,'carrierAggrSensorEntry':carrierAggrSensorEntry,_F:carrierAggrSensorIndex,'carrierAggrSensorRowstatus':carrierAggrSensorRowstatus,'carrierAggrSensorAdminStatus':carrierAggrSensorAdminStatus,'carrierAggrSensorIfIndex':carrierAggrSensorIfIndex,'carrierAggrSensorHitlessCapability':carrierAggrSensorHitlessCapability,'carrierAggrSensorHitlessBehaviour':carrierAggrSensorHitlessBehaviour,'carrierAggrSensorHitlessMode':carrierAggrSensorHitlessMode,'carrierAggrSensorHitlessProfile':carrierAggrSensorHitlessProfile,'carrierAggrSensorHitlessStatus':carrierAggrSensorHitlessStatus,'carrierAggrActuatorTable':carrierAggrActuatorTable,'carrierAggrActuatorEntry':carrierAggrActuatorEntry,_G:carrierAggrActuatorIndex,'carrierAggrActuatorRowStatus':carrierAggrActuatorRowStatus,'carrierAggrActuatorAdminStatus':carrierAggrActuatorAdminStatus,'carrierAggrActuatorIfIndex':carrierAggrActuatorIfIndex,'carrierAggrActuatorSensorIndex':carrierAggrActuatorSensorIndex,'carrierAggrActuatorConcIpAddr':carrierAggrActuatorConcIpAddr})