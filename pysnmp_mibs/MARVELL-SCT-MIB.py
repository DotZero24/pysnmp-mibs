_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlSctMib=ModuleIdentity((1,3,6,1,4,1,89,203))
_RlSctCpuRateEnabled_Type=TruthValue
_RlSctCpuRateEnabled_Object=MibScalar
rlSctCpuRateEnabled=_RlSctCpuRateEnabled_Object((1,3,6,1,4,1,89,203,1),_RlSctCpuRateEnabled_Type())
rlSctCpuRateEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlSctCpuRateEnabled.setStatus(_A)
_RlSctCpuRate_Type=Counter32
_RlSctCpuRate_Object=MibScalar
rlSctCpuRate=_RlSctCpuRate_Object((1,3,6,1,4,1,89,203,2),_RlSctCpuRate_Type())
rlSctCpuRate.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlSctCpuRate.setStatus(_A)
mibBuilder.exportSymbols('MARVELL-SCT-MIB',**{'rlSctMib':rlSctMib,'rlSctCpuRateEnabled':rlSctCpuRateEnabled,'rlSctCpuRate':rlSctCpuRate})