_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mellanoxPowerCycle,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxPowerCycle')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxPowerCycleMib=ModuleIdentity((1,3,6,1,4,1,33049,10,1))
if mibBuilder.loadTexts:mellanoxPowerCycleMib.setRevisions(('2018-06-04 00:00',))
_MellanoxPowerCycleMibObjects_ObjectIdentity=ObjectIdentity
mellanoxPowerCycleMibObjects=_MellanoxPowerCycleMibObjects_ObjectIdentity((1,3,6,1,4,1,33049,10,1,1))
_MellanoxPowerCycleCmd_ObjectIdentity=ObjectIdentity
mellanoxPowerCycleCmd=_MellanoxPowerCycleCmd_ObjectIdentity((1,3,6,1,4,1,33049,10,1,1,2))
class _MellanoxPowerCycleCmdExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mellanoxPowerCycleCmdExecuteReload',1),('mellanoxPowerCycleCmdExecuteReloadDiscard',2),('mellanoxPowerCycleCmdExecuteReloadForce',3),('mellanoxPowerCycleCmdExecuteReloadSlave',4)))
_MellanoxPowerCycleCmdExecute_Type.__name__=_B
_MellanoxPowerCycleCmdExecute_Object=MibScalar
mellanoxPowerCycleCmdExecute=_MellanoxPowerCycleCmdExecute_Object((1,3,6,1,4,1,33049,10,1,1,2,1),_MellanoxPowerCycleCmdExecute_Type())
mellanoxPowerCycleCmdExecute.setMaxAccess('read-write')
if mibBuilder.loadTexts:mellanoxPowerCycleCmdExecute.setStatus(_A)
_MellanoxPowerCycleCmdStatus_Type=Integer32
_MellanoxPowerCycleCmdStatus_Object=MibScalar
mellanoxPowerCycleCmdStatus=_MellanoxPowerCycleCmdStatus_Object((1,3,6,1,4,1,33049,10,1,1,2,2),_MellanoxPowerCycleCmdStatus_Type())
mellanoxPowerCycleCmdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mellanoxPowerCycleCmdStatus.setStatus(_A)
_MellanoxPowerCycleCmdStatusString_Type=OctetString
_MellanoxPowerCycleCmdStatusString_Object=MibScalar
mellanoxPowerCycleCmdStatusString=_MellanoxPowerCycleCmdStatusString_Object((1,3,6,1,4,1,33049,10,1,1,2,3),_MellanoxPowerCycleCmdStatusString_Type())
mellanoxPowerCycleCmdStatusString.setMaxAccess(_C)
if mibBuilder.loadTexts:mellanoxPowerCycleCmdStatusString.setStatus(_A)
_MellanoxPowerCycleNotifications_ObjectIdentity=ObjectIdentity
mellanoxPowerCycleNotifications=_MellanoxPowerCycleNotifications_ObjectIdentity((1,3,6,1,4,1,33049,10,1,1,3))
mellanoxPowerCyclePlannedReload=NotificationType((1,3,6,1,4,1,33049,10,1,1,3,1))
if mibBuilder.loadTexts:mellanoxPowerCyclePlannedReload.setStatus(_A)
mibBuilder.exportSymbols('MELLANOX-POWER-CYCLE-MIB',**{'mellanoxPowerCycleMib':mellanoxPowerCycleMib,'mellanoxPowerCycleMibObjects':mellanoxPowerCycleMibObjects,'mellanoxPowerCycleCmd':mellanoxPowerCycleCmd,'mellanoxPowerCycleCmdExecute':mellanoxPowerCycleCmdExecute,'mellanoxPowerCycleCmdStatus':mellanoxPowerCycleCmdStatus,'mellanoxPowerCycleCmdStatusString':mellanoxPowerCycleCmdStatusString,'mellanoxPowerCycleNotifications':mellanoxPowerCycleNotifications,'mellanoxPowerCyclePlannedReload':mellanoxPowerCyclePlannedReload})