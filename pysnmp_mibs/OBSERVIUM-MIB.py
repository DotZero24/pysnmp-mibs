_B='read-only'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_A,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
_Observium_ObjectIdentity=ObjectIdentity
observium=_Observium_ObjectIdentity((1,3,6,1,4,1,36602))
_ObsObjects_ObjectIdentity=ObjectIdentity
obsObjects=_ObsObjects_ObjectIdentity((1,3,6,1,4,1,36602,1))
_ObsHostInfo_ObjectIdentity=ObjectIdentity
obsHostInfo=_ObsHostInfo_ObjectIdentity((1,3,6,1,4,1,36602,1,1))
class _ObsLinuxDistro_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ObsLinuxDistro_Type.__name__=_A
_ObsLinuxDistro_Object=MibScalar
obsLinuxDistro=_ObsLinuxDistro_Object((1,3,6,1,4,1,36602,1,1,2),_ObsLinuxDistro_Type())
obsLinuxDistro.setMaxAccess(_B)
if mibBuilder.loadTexts:obsLinuxDistro.setStatus('current')
_ObsCPUUsage_Type=Integer32
_ObsCPUUsage_Object=MibScalar
obsCPUUsage=_ObsCPUUsage_Object((1,3,6,1,4,1,36602,1,1,3),_ObsCPUUsage_Type())
obsCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:obsCPUUsage.setStatus('mandatory')
mibBuilder.exportSymbols('OBSERVIUM-MIB',**{'observium':observium,'obsObjects':obsObjects,'obsHostInfo':obsHostInfo,'obsLinuxDistro':obsLinuxDistro,'obsCPUUsage':obsCPUUsage})