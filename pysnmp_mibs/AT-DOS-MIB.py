_K='seconds'
_J='disabled'
_I='enabled'
_H='none'
_G='Bits'
_F='dosDefenseAttackType'
_E='dosDefensePort'
_D='AT-DOS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,_G,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dosDefense=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,143))
class _DosDefenseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_DosDefenseStatus_Type.__name__=_C
_DosDefenseStatus_Object=MibScalar
dosDefenseStatus=_DosDefenseStatus_Object((1,3,6,1,4,1,207,8,4,4,4,143,1),_DosDefenseStatus_Type())
dosDefenseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseStatus.setStatus(_A)
class _DosDefenseDebugMode_Type(Bits):namedValues=NamedValues(*((_H,0),('packet',1),('attack',2),('packet-attack',3),('diagnostics',4),('packet-diagnostics',5),('attack-diagnostics',6),('packet-attack-diagnostics',7)))
_DosDefenseDebugMode_Type.__name__=_G
_DosDefenseDebugMode_Object=MibScalar
dosDefenseDebugMode=_DosDefenseDebugMode_Object((1,3,6,1,4,1,207,8,4,4,4,143,2),_DosDefenseDebugMode_Type())
dosDefenseDebugMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseDebugMode.setStatus(_A)
class _DosDefenseNumDebugPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('continuous',0))
_DosDefenseNumDebugPackets_Type.__name__=_C
_DosDefenseNumDebugPackets_Object=MibScalar
dosDefenseNumDebugPackets=_DosDefenseNumDebugPackets_Object((1,3,6,1,4,1,207,8,4,4,4,143,3),_DosDefenseNumDebugPackets_Type())
dosDefenseNumDebugPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseNumDebugPackets.setStatus(_A)
_DosDefenseTable_Object=MibTable
dosDefenseTable=_DosDefenseTable_Object((1,3,6,1,4,1,207,8,4,4,4,143,4))
if mibBuilder.loadTexts:dosDefenseTable.setStatus(_A)
_DosDefenseEntry_Object=MibTableRow
dosDefenseEntry=_DosDefenseEntry_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1))
dosDefenseEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:dosDefenseEntry.setStatus(_A)
class _DosDefensePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_DosDefensePort_Type.__name__=_C
_DosDefensePort_Object=MibTableColumn
dosDefensePort=_DosDefensePort_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,1),_DosDefensePort_Type())
dosDefensePort.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefensePort.setStatus(_A)
class _DosDefenseAttackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('synFlood',1),('pingOfDeath',2),('smurf',3),('ipOptions',4),('land',5),('teardrop',6),(_H,7)))
_DosDefenseAttackType_Type.__name__=_C
_DosDefenseAttackType_Object=MibTableColumn
dosDefenseAttackType=_DosDefenseAttackType_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,2),_DosDefenseAttackType_Type())
dosDefenseAttackType.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseAttackType.setStatus(_A)
class _DosDefenseDefenseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('set',3)))
_DosDefenseDefenseStatus_Type.__name__=_C
_DosDefenseDefenseStatus_Object=MibTableColumn
dosDefenseDefenseStatus=_DosDefenseDefenseStatus_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,3),_DosDefenseDefenseStatus_Type())
dosDefenseDefenseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseDefenseStatus.setStatus(_A)
class _DosDefenseThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_DosDefenseThreshold_Type.__name__=_C
_DosDefenseThreshold_Object=MibTableColumn
dosDefenseThreshold=_DosDefenseThreshold_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,4),_DosDefenseThreshold_Type())
dosDefenseThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseThreshold.setStatus(_A)
class _DosDefenseBlockTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DosDefenseBlockTime_Type.__name__=_C
_DosDefenseBlockTime_Object=MibTableColumn
dosDefenseBlockTime=_DosDefenseBlockTime_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,5),_DosDefenseBlockTime_Type())
dosDefenseBlockTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseBlockTime.setStatus(_A)
if mibBuilder.loadTexts:dosDefenseBlockTime.setUnits(_K)
_DosDefenseMirroring_Type=TruthValue
_DosDefenseMirroring_Object=MibTableColumn
dosDefenseMirroring=_DosDefenseMirroring_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,6),_DosDefenseMirroring_Type())
dosDefenseMirroring.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseMirroring.setStatus(_A)
class _DosDefensePortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notApplicable',0),('client',1),('gateway',2)))
_DosDefensePortType_Type.__name__=_C
_DosDefensePortType_Object=MibTableColumn
dosDefensePortType=_DosDefensePortType_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,7),_DosDefensePortType_Type())
dosDefensePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefensePortType.setStatus(_A)
_DosDefenseSubnetAddress_Type=IpAddress
_DosDefenseSubnetAddress_Object=MibTableColumn
dosDefenseSubnetAddress=_DosDefenseSubnetAddress_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,8),_DosDefenseSubnetAddress_Type())
dosDefenseSubnetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseSubnetAddress.setStatus(_A)
_DosDefenseSubnetMask_Type=IpAddress
_DosDefenseSubnetMask_Object=MibTableColumn
dosDefenseSubnetMask=_DosDefenseSubnetMask_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,9),_DosDefenseSubnetMask_Type())
dosDefenseSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseSubnetMask.setStatus(_A)
class _DosDefenseAttackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('suspected',1),('inProgress',2)))
_DosDefenseAttackState_Type.__name__=_C
_DosDefenseAttackState_Object=MibTableColumn
dosDefenseAttackState=_DosDefenseAttackState_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,10),_DosDefenseAttackState_Type())
dosDefenseAttackState.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseAttackState.setStatus(_A)
_DosDefenseAttackCount_Type=Counter32
_DosDefenseAttackCount_Object=MibTableColumn
dosDefenseAttackCount=_DosDefenseAttackCount_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,11),_DosDefenseAttackCount_Type())
dosDefenseAttackCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseAttackCount.setStatus(_A)
class _DosDefenseRemainingBlockTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DosDefenseRemainingBlockTime_Type.__name__=_C
_DosDefenseRemainingBlockTime_Object=MibTableColumn
dosDefenseRemainingBlockTime=_DosDefenseRemainingBlockTime_Object((1,3,6,1,4,1,207,8,4,4,4,143,4,1,12),_DosDefenseRemainingBlockTime_Type())
dosDefenseRemainingBlockTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dosDefenseRemainingBlockTime.setStatus(_A)
if mibBuilder.loadTexts:dosDefenseRemainingBlockTime.setUnits(_K)
_DosDefenseTraps_ObjectIdentity=ObjectIdentity
dosDefenseTraps=_DosDefenseTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,143,5))
dosDefenseAttackStart=NotificationType((1,3,6,1,4,1,207,8,4,4,4,143,5,1))
dosDefenseAttackStart.setObjects(*((_D,_E),(_D,_F)))
if mibBuilder.loadTexts:dosDefenseAttackStart.setStatus(_A)
dosDefenseAttackEnd=NotificationType((1,3,6,1,4,1,207,8,4,4,4,143,5,2))
dosDefenseAttackEnd.setObjects(*((_D,_E),(_D,_F)))
if mibBuilder.loadTexts:dosDefenseAttackEnd.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'dosDefense':dosDefense,'dosDefenseStatus':dosDefenseStatus,'dosDefenseDebugMode':dosDefenseDebugMode,'dosDefenseNumDebugPackets':dosDefenseNumDebugPackets,'dosDefenseTable':dosDefenseTable,'dosDefenseEntry':dosDefenseEntry,_E:dosDefensePort,_F:dosDefenseAttackType,'dosDefenseDefenseStatus':dosDefenseDefenseStatus,'dosDefenseThreshold':dosDefenseThreshold,'dosDefenseBlockTime':dosDefenseBlockTime,'dosDefenseMirroring':dosDefenseMirroring,'dosDefensePortType':dosDefensePortType,'dosDefenseSubnetAddress':dosDefenseSubnetAddress,'dosDefenseSubnetMask':dosDefenseSubnetMask,'dosDefenseAttackState':dosDefenseAttackState,'dosDefenseAttackCount':dosDefenseAttackCount,'dosDefenseRemainingBlockTime':dosDefenseRemainingBlockTime,'dosDefenseTraps':dosDefenseTraps,'dosDefenseAttackStart':dosDefenseAttackStart,'dosDefenseAttackEnd':dosDefenseAttackEnd})