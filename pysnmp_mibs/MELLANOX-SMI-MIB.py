_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanox=ModuleIdentity((1,3,6,1,4,1,33049))
if mibBuilder.loadTexts:mellanox.setRevisions(('2016-07-26 00:00',))
_MellanoxProducts_ObjectIdentity=ObjectIdentity
mellanoxProducts=_MellanoxProducts_ObjectIdentity((1,3,6,1,4,1,33049,1))
if mibBuilder.loadTexts:mellanoxProducts.setStatus(_A)
_MellanoxIfVPI_ObjectIdentity=ObjectIdentity
mellanoxIfVPI=_MellanoxIfVPI_ObjectIdentity((1,3,6,1,4,1,33049,3))
if mibBuilder.loadTexts:mellanoxIfVPI.setStatus(_A)
_MellanoxUFMTrap_ObjectIdentity=ObjectIdentity
mellanoxUFMTrap=_MellanoxUFMTrap_ObjectIdentity((1,3,6,1,4,1,33049,4))
if mibBuilder.loadTexts:mellanoxUFMTrap.setStatus(_A)
_MellanoxEntity_ObjectIdentity=ObjectIdentity
mellanoxEntity=_MellanoxEntity_ObjectIdentity((1,3,6,1,4,1,33049,5))
if mibBuilder.loadTexts:mellanoxEntity.setStatus(_A)
_MellanoxEntState_ObjectIdentity=ObjectIdentity
mellanoxEntState=_MellanoxEntState_ObjectIdentity((1,3,6,1,4,1,33049,7))
if mibBuilder.loadTexts:mellanoxEntState.setStatus(_A)
_MellanoxDCBTraps_ObjectIdentity=ObjectIdentity
mellanoxDCBTraps=_MellanoxDCBTraps_ObjectIdentity((1,3,6,1,4,1,33049,8))
if mibBuilder.loadTexts:mellanoxDCBTraps.setStatus(_A)
_MellanoxPowerCycle_ObjectIdentity=ObjectIdentity
mellanoxPowerCycle=_MellanoxPowerCycle_ObjectIdentity((1,3,6,1,4,1,33049,10))
if mibBuilder.loadTexts:mellanoxPowerCycle.setStatus(_A)
_MellanoxSWUpdate_ObjectIdentity=ObjectIdentity
mellanoxSWUpdate=_MellanoxSWUpdate_ObjectIdentity((1,3,6,1,4,1,33049,11))
if mibBuilder.loadTexts:mellanoxSWUpdate.setStatus(_A)
_MellanoxConfigDB_ObjectIdentity=ObjectIdentity
mellanoxConfigDB=_MellanoxConfigDB_ObjectIdentity((1,3,6,1,4,1,33049,12))
if mibBuilder.loadTexts:mellanoxConfigDB.setStatus(_A)
_MellanoxXstp_ObjectIdentity=ObjectIdentity
mellanoxXstp=_MellanoxXstp_ObjectIdentity((1,3,6,1,4,1,33049,13))
if mibBuilder.loadTexts:mellanoxXstp.setStatus(_A)
_MellanoxVRF_ObjectIdentity=ObjectIdentity
mellanoxVRF=_MellanoxVRF_ObjectIdentity((1,3,6,1,4,1,33049,14))
if mibBuilder.loadTexts:mellanoxVRF.setStatus(_A)
_MellanoxQoS_ObjectIdentity=ObjectIdentity
mellanoxQoS=_MellanoxQoS_ObjectIdentity((1,3,6,1,4,1,33049,15))
if mibBuilder.loadTexts:mellanoxQoS.setStatus(_A)
mibBuilder.exportSymbols('MELLANOX-SMI-MIB',**{'mellanox':mellanox,'mellanoxProducts':mellanoxProducts,'mellanoxIfVPI':mellanoxIfVPI,'mellanoxUFMTrap':mellanoxUFMTrap,'mellanoxEntity':mellanoxEntity,'mellanoxEntState':mellanoxEntState,'mellanoxDCBTraps':mellanoxDCBTraps,'mellanoxPowerCycle':mellanoxPowerCycle,'mellanoxSWUpdate':mellanoxSWUpdate,'mellanoxConfigDB':mellanoxConfigDB,'mellanoxXstp':mellanoxXstp,'mellanoxVRF':mellanoxVRF,'mellanoxQoS':mellanoxQoS})