_D='TruthValue'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
rlSafeGuard=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,131))
if mibBuilder.loadTexts:rlSafeGuard.setRevisions(('2007-11-18 00:00',))
class _RlSafeGuardEnabled_Type(TruthValue):defaultValue=2
_RlSafeGuardEnabled_Type.__name__=_D
_RlSafeGuardEnabled_Object=MibScalar
rlSafeGuardEnabled=_RlSafeGuardEnabled_Object((1,3,6,1,4,1,171,10,94,89,89,131,1),_RlSafeGuardEnabled_Type())
rlSafeGuardEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSafeGuardEnabled.setStatus(_B)
class _RlSafeGuardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('attack',1)))
_RlSafeGuardStatus_Type.__name__=_A
_RlSafeGuardStatus_Object=MibScalar
rlSafeGuardStatus=_RlSafeGuardStatus_Object((1,3,6,1,4,1,171,10,94,89,89,131,2),_RlSafeGuardStatus_Type())
rlSafeGuardStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlSafeGuardStatus.setStatus(_B)
class _RlSafeGuardCpuUtilizationUpper_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RlSafeGuardCpuUtilizationUpper_Type.__name__=_A
_RlSafeGuardCpuUtilizationUpper_Object=MibScalar
rlSafeGuardCpuUtilizationUpper=_RlSafeGuardCpuUtilizationUpper_Object((1,3,6,1,4,1,171,10,94,89,89,131,3),_RlSafeGuardCpuUtilizationUpper_Type())
rlSafeGuardCpuUtilizationUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSafeGuardCpuUtilizationUpper.setStatus(_B)
class _RlSafeGuardCpuUtilizationLower_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RlSafeGuardCpuUtilizationLower_Type.__name__=_A
_RlSafeGuardCpuUtilizationLower_Object=MibScalar
rlSafeGuardCpuUtilizationLower=_RlSafeGuardCpuUtilizationLower_Object((1,3,6,1,4,1,171,10,94,89,89,131,4),_RlSafeGuardCpuUtilizationLower_Type())
rlSafeGuardCpuUtilizationLower.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSafeGuardCpuUtilizationLower.setStatus(_B)
class _RlSafeGuardBroadcastRateUpper_Type(Integer32):defaultValue=350;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,1000))
_RlSafeGuardBroadcastRateUpper_Type.__name__=_A
_RlSafeGuardBroadcastRateUpper_Object=MibScalar
rlSafeGuardBroadcastRateUpper=_RlSafeGuardBroadcastRateUpper_Object((1,3,6,1,4,1,171,10,94,89,89,131,5),_RlSafeGuardBroadcastRateUpper_Type())
rlSafeGuardBroadcastRateUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSafeGuardBroadcastRateUpper.setStatus(_B)
class _RlSafeGuardBroadcastRateLower_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,1000))
_RlSafeGuardBroadcastRateLower_Type.__name__=_A
_RlSafeGuardBroadcastRateLower_Object=MibScalar
rlSafeGuardBroadcastRateLower=_RlSafeGuardBroadcastRateLower_Object((1,3,6,1,4,1,171,10,94,89,89,131,6),_RlSafeGuardBroadcastRateLower_Type())
rlSafeGuardBroadcastRateLower.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSafeGuardBroadcastRateLower.setStatus(_B)
mibBuilder.exportSymbols('DLINK-3100-SAFE-GUARD-MIB',**{'rlSafeGuard':rlSafeGuard,'rlSafeGuardEnabled':rlSafeGuardEnabled,'rlSafeGuardStatus':rlSafeGuardStatus,'rlSafeGuardCpuUtilizationUpper':rlSafeGuardCpuUtilizationUpper,'rlSafeGuardCpuUtilizationLower':rlSafeGuardCpuUtilizationLower,'rlSafeGuardBroadcastRateUpper':rlSafeGuardBroadcastRateUpper,'rlSafeGuardBroadcastRateLower':rlSafeGuardBroadcastRateLower})