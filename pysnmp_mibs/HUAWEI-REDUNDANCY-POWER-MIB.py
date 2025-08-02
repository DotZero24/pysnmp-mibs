_K='redundancyFanStatus'
_J='redundancyPowerPreviousStatus'
_I='redundancyPowerStatus'
_H='redundancyFanID'
_G='fail'
_F='normal'
_E='redundancyPowerID'
_D='Integer32'
_C='read-only'
_B='HUAWEI-REDUNDANCY-POWER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mlsr,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','mlsr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
redundancyPower=ModuleIdentity((1,3,6,1,4,1,2011,2,33,4))
_RedundancyPowerTable_Object=MibTable
redundancyPowerTable=_RedundancyPowerTable_Object((1,3,6,1,4,1,2011,2,33,4,1))
if mibBuilder.loadTexts:redundancyPowerTable.setStatus(_A)
_RedundancyPowerEntry_Object=MibTableRow
redundancyPowerEntry=_RedundancyPowerEntry_Object((1,3,6,1,4,1,2011,2,33,4,1,1))
redundancyPowerEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:redundancyPowerEntry.setStatus(_A)
_RedundancyPowerID_Type=Integer32
_RedundancyPowerID_Object=MibTableColumn
redundancyPowerID=_RedundancyPowerID_Object((1,3,6,1,4,1,2011,2,33,4,1,1,1),_RedundancyPowerID_Type())
redundancyPowerID.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyPowerID.setStatus(_A)
class _RedundancyPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('space',1),(_F,2),(_G,3)))
_RedundancyPowerStatus_Type.__name__=_D
_RedundancyPowerStatus_Object=MibTableColumn
redundancyPowerStatus=_RedundancyPowerStatus_Object((1,3,6,1,4,1,2011,2,33,4,1,1,2),_RedundancyPowerStatus_Type())
redundancyPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyPowerStatus.setStatus(_A)
class _RedundancyPowerPreviousStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('space',1),(_F,2),(_G,3)))
_RedundancyPowerPreviousStatus_Type.__name__=_D
_RedundancyPowerPreviousStatus_Object=MibTableColumn
redundancyPowerPreviousStatus=_RedundancyPowerPreviousStatus_Object((1,3,6,1,4,1,2011,2,33,4,1,1,3),_RedundancyPowerPreviousStatus_Type())
redundancyPowerPreviousStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyPowerPreviousStatus.setStatus(_A)
_PowerTraps_ObjectIdentity=ObjectIdentity
powerTraps=_PowerTraps_ObjectIdentity((1,3,6,1,4,1,2011,2,33,4,2))
_RedundancyFan_ObjectIdentity=ObjectIdentity
redundancyFan=_RedundancyFan_ObjectIdentity((1,3,6,1,4,1,2011,2,33,5))
_RedundancyFanTable_Object=MibTable
redundancyFanTable=_RedundancyFanTable_Object((1,3,6,1,4,1,2011,2,33,5,1))
if mibBuilder.loadTexts:redundancyFanTable.setStatus(_A)
_RedundancyFanEntry_Object=MibTableRow
redundancyFanEntry=_RedundancyFanEntry_Object((1,3,6,1,4,1,2011,2,33,5,1,1))
redundancyFanEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:redundancyFanEntry.setStatus(_A)
_RedundancyFanID_Type=Integer32
_RedundancyFanID_Object=MibTableColumn
redundancyFanID=_RedundancyFanID_Object((1,3,6,1,4,1,2011,2,33,5,1,1,1),_RedundancyFanID_Type())
redundancyFanID.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyFanID.setStatus(_A)
class _RedundancyFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RedundancyFanStatus_Type.__name__=_D
_RedundancyFanStatus_Object=MibTableColumn
redundancyFanStatus=_RedundancyFanStatus_Object((1,3,6,1,4,1,2011,2,33,5,1,1,2),_RedundancyFanStatus_Type())
redundancyFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:redundancyFanStatus.setStatus(_A)
_FanTraps_ObjectIdentity=ObjectIdentity
fanTraps=_FanTraps_ObjectIdentity((1,3,6,1,4,1,2011,2,33,5,2))
powerStatusChangedTrap=NotificationType((1,3,6,1,4,1,2011,2,33,4,2,1))
powerStatusChangedTrap.setObjects(*((_B,_E),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:powerStatusChangedTrap.setStatus(_A)
fanStatusChangedTrap=NotificationType((1,3,6,1,4,1,2011,2,33,5,2,1))
fanStatusChangedTrap.setObjects(*((_B,_H),(_B,_K)))
if mibBuilder.loadTexts:fanStatusChangedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'redundancyPower':redundancyPower,'redundancyPowerTable':redundancyPowerTable,'redundancyPowerEntry':redundancyPowerEntry,_E:redundancyPowerID,_I:redundancyPowerStatus,_J:redundancyPowerPreviousStatus,'powerTraps':powerTraps,'powerStatusChangedTrap':powerStatusChangedTrap,'redundancyFan':redundancyFan,'redundancyFanTable':redundancyFanTable,'redundancyFanEntry':redundancyFanEntry,_H:redundancyFanID,_K:redundancyFanStatus,'fanTraps':fanTraps,'fanStatusChangedTrap':fanStatusChangedTrap})