_G='highpower'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='milliwatts'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cumulusMib,=mibBuilder.importSymbols('CUMULUS-SNMP-MIB','cumulusMib')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
poeMIBObjects=ModuleIdentity((1,3,6,1,4,1,40310,3))
if mibBuilder.loadTexts:poeMIBObjects.setRevisions(('2016-07-12 00:00',))
class MilliValue(TextualConvention,Integer32):status=_A;displayHint='d'
_PoeSystemValues_ObjectIdentity=ObjectIdentity
poeSystemValues=_PoeSystemValues_ObjectIdentity((1,3,6,1,4,1,40310,3,1))
_PoeTotalSystemPower_Type=MilliValue
_PoeTotalSystemPower_Object=MibScalar
poeTotalSystemPower=_PoeTotalSystemPower_Object((1,3,6,1,4,1,40310,3,1,1),_PoeTotalSystemPower_Type())
poeTotalSystemPower.setMaxAccess(_B)
if mibBuilder.loadTexts:poeTotalSystemPower.setStatus(_A)
if mibBuilder.loadTexts:poeTotalSystemPower.setUnits(_C)
_PoeTotalUsedPower_Type=MilliValue
_PoeTotalUsedPower_Object=MibScalar
poeTotalUsedPower=_PoeTotalUsedPower_Object((1,3,6,1,4,1,40310,3,1,2),_PoeTotalUsedPower_Type())
poeTotalUsedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:poeTotalUsedPower.setStatus(_A)
if mibBuilder.loadTexts:poeTotalUsedPower.setUnits(_C)
_PoeTotalAvailablePower_Type=MilliValue
_PoeTotalAvailablePower_Object=MibScalar
poeTotalAvailablePower=_PoeTotalAvailablePower_Object((1,3,6,1,4,1,40310,3,1,3),_PoeTotalAvailablePower_Type())
poeTotalAvailablePower.setMaxAccess(_B)
if mibBuilder.loadTexts:poeTotalAvailablePower.setStatus(_A)
if mibBuilder.loadTexts:poeTotalAvailablePower.setUnits(_C)
_PoeLastUpdateTime_Type=TimeStamp
_PoeLastUpdateTime_Object=MibScalar
poeLastUpdateTime=_PoeLastUpdateTime_Object((1,3,6,1,4,1,40310,3,1,4),_PoeLastUpdateTime_Type())
poeLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:poeLastUpdateTime.setStatus(_A)
_PoeObjectsTable_Object=MibTable
poeObjectsTable=_PoeObjectsTable_Object((1,3,6,1,4,1,40310,3,2))
if mibBuilder.loadTexts:poeObjectsTable.setStatus(_A)
_PoeObjectsEntry_Object=MibTableRow
poeObjectsEntry=_PoeObjectsEntry_Object((1,3,6,1,4,1,40310,3,2,1))
poeObjectsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:poeObjectsEntry.setStatus(_A)
_PortName_Type=DisplayString
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,40310,3,2,1,1),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('high',2),('critical',3)))
_PortPriority_Type.__name__=_D
_PortPriority_Object=MibTableColumn
portPriority=_PortPriority_Object((1,3,6,1,4,1,40310,3,2,1,2),_PortPriority_Type())
portPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:portPriority.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('ieee802Dot3af',2),('ieee802Dot3at',3),('legacy',4),(_G,5),('invalid',6),('ieee802Dot3afat',7)))
_PortType_Type.__name__=_D
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,40310,3,2,1,3),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('disabled',2),('searching',3),('connected',4),('powerdenied',5),('fault',6)))
_PortStatus_Type.__name__=_D
_PortStatus_Object=MibTableColumn
portStatus=_PortStatus_Object((1,3,6,1,4,1,40310,3,2,1,4),_PortStatus_Type())
portStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatus.setStatus(_A)
class _PortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('default',0),('verylowpower',1),('lowpower',2),('midpower',3),(_G,4)))
_PortClass_Type.__name__=_D
_PortClass_Object=MibTableColumn
portClass=_PortClass_Object((1,3,6,1,4,1,40310,3,2,1,5),_PortClass_Type())
portClass.setMaxAccess(_B)
if mibBuilder.loadTexts:portClass.setStatus(_A)
class _PortFourPairModeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_PortFourPairModeEnabled_Type.__name__=_D
_PortFourPairModeEnabled_Object=MibTableColumn
portFourPairModeEnabled=_PortFourPairModeEnabled_Object((1,3,6,1,4,1,40310,3,2,1,6),_PortFourPairModeEnabled_Type())
portFourPairModeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:portFourPairModeEnabled.setStatus(_A)
_PortVoltage_Type=MilliValue
_PortVoltage_Object=MibTableColumn
portVoltage=_PortVoltage_Object((1,3,6,1,4,1,40310,3,2,1,7),_PortVoltage_Type())
portVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:portVoltage.setStatus(_A)
if mibBuilder.loadTexts:portVoltage.setUnits('millivolts')
_PortCurrent_Type=MilliValue
_PortCurrent_Object=MibTableColumn
portCurrent=_PortCurrent_Object((1,3,6,1,4,1,40310,3,2,1,8),_PortCurrent_Type())
portCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:portCurrent.setStatus(_A)
if mibBuilder.loadTexts:portCurrent.setUnits('milliamps')
_PortPower_Type=MilliValue
_PortPower_Object=MibTableColumn
portPower=_PortPower_Object((1,3,6,1,4,1,40310,3,2,1,9),_PortPower_Type())
portPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portPower.setStatus(_A)
if mibBuilder.loadTexts:portPower.setUnits(_C)
_PortMaxPower_Type=MilliValue
_PortMaxPower_Object=MibTableColumn
portMaxPower=_PortMaxPower_Object((1,3,6,1,4,1,40310,3,2,1,10),_PortMaxPower_Type())
portMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portMaxPower.setStatus(_A)
if mibBuilder.loadTexts:portMaxPower.setUnits(_C)
_PortAllocatedPower_Type=MilliValue
_PortAllocatedPower_Object=MibTableColumn
portAllocatedPower=_PortAllocatedPower_Object((1,3,6,1,4,1,40310,3,2,1,11),_PortAllocatedPower_Type())
portAllocatedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portAllocatedPower.setStatus(_A)
if mibBuilder.loadTexts:portAllocatedPower.setUnits(_C)
_LldpRequestedPower_Type=MilliValue
_LldpRequestedPower_Object=MibTableColumn
lldpRequestedPower=_LldpRequestedPower_Object((1,3,6,1,4,1,40310,3,2,1,12),_LldpRequestedPower_Type())
lldpRequestedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRequestedPower.setStatus(_A)
if mibBuilder.loadTexts:lldpRequestedPower.setUnits(_C)
_LldpAllocatedPower_Type=MilliValue
_LldpAllocatedPower_Object=MibTableColumn
lldpAllocatedPower=_LldpAllocatedPower_Object((1,3,6,1,4,1,40310,3,2,1,13),_LldpAllocatedPower_Type())
lldpAllocatedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpAllocatedPower.setStatus(_A)
if mibBuilder.loadTexts:lldpAllocatedPower.setUnits(_C)
mibBuilder.exportSymbols('CUMULUS-POE-MIB',**{'MilliValue':MilliValue,'poeMIBObjects':poeMIBObjects,'poeSystemValues':poeSystemValues,'poeTotalSystemPower':poeTotalSystemPower,'poeTotalUsedPower':poeTotalUsedPower,'poeTotalAvailablePower':poeTotalAvailablePower,'poeLastUpdateTime':poeLastUpdateTime,'poeObjectsTable':poeObjectsTable,'poeObjectsEntry':poeObjectsEntry,'portName':portName,'portPriority':portPriority,'portType':portType,'portStatus':portStatus,'portClass':portClass,'portFourPairModeEnabled':portFourPairModeEnabled,'portVoltage':portVoltage,'portCurrent':portCurrent,'portPower':portPower,'portMaxPower':portMaxPower,'portAllocatedPower':portAllocatedPower,'lldpRequestedPower':lldpRequestedPower,'lldpAllocatedPower':lldpAllocatedPower})