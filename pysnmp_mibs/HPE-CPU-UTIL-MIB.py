_G='hpeSwitchMinCPUThreshold'
_F='hpeSwitchMaxCPUThreshold'
_E='read-write'
_D='hpeSwitchAverageCPUUtilization'
_C='Integer32'
_B='HPE-CPU-UTIL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpVCSE_40Gb_F8_Module,=mibBuilder.importSymbols('HPSVRMGMT-OID','hpVCSE-40Gb-F8-Module')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpeCpuUtilMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4130))
if mibBuilder.loadTexts:hpeCpuUtilMIB.setRevisions(('2019-12-19 00:00',))
_HpeSynergyCpuUtilMIBObjects_ObjectIdentity=ObjectIdentity
hpeSynergyCpuUtilMIBObjects=_HpeSynergyCpuUtilMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1))
_HpeCpuUtilConfig_ObjectIdentity=ObjectIdentity
hpeCpuUtilConfig=_HpeCpuUtilConfig_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4130,1))
class _HpeSwitchMaxCPUThreshold_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpeSwitchMaxCPUThreshold_Type.__name__=_C
_HpeSwitchMaxCPUThreshold_Object=MibScalar
hpeSwitchMaxCPUThreshold=_HpeSwitchMaxCPUThreshold_Object((1,3,6,1,4,1,11,5,7,5,8,1,4130,1,1),_HpeSwitchMaxCPUThreshold_Type())
hpeSwitchMaxCPUThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeSwitchMaxCPUThreshold.setStatus(_A)
class _HpeSwitchMinCPUThreshold_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpeSwitchMinCPUThreshold_Type.__name__=_C
_HpeSwitchMinCPUThreshold_Object=MibScalar
hpeSwitchMinCPUThreshold=_HpeSwitchMinCPUThreshold_Object((1,3,6,1,4,1,11,5,7,5,8,1,4130,1,2),_HpeSwitchMinCPUThreshold_Type())
hpeSwitchMinCPUThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeSwitchMinCPUThreshold.setStatus(_A)
_HpeCpuUtiStatus_ObjectIdentity=ObjectIdentity
hpeCpuUtiStatus=_HpeCpuUtiStatus_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4130,2))
_HpeSwitchAverageCPUUtilization_Type=Integer32
_HpeSwitchAverageCPUUtilization_Object=MibScalar
hpeSwitchAverageCPUUtilization=_HpeSwitchAverageCPUUtilization_Object((1,3,6,1,4,1,11,5,7,5,8,1,4130,2,1),_HpeSwitchAverageCPUUtilization_Type())
hpeSwitchAverageCPUUtilization.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpeSwitchAverageCPUUtilization.setStatus(_A)
if mibBuilder.loadTexts:hpeSwitchAverageCPUUtilization.setUnits('percentage')
_HpeCpuUtilTraps_ObjectIdentity=ObjectIdentity
hpeCpuUtilTraps=_HpeCpuUtilTraps_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4130,3))
hpeTrapMaxCPUThreshold=NotificationType((1,3,6,1,4,1,11,5,7,5,8,1,4130,3,1))
hpeTrapMaxCPUThreshold.setObjects(*((_B,_F),(_B,_D)))
if mibBuilder.loadTexts:hpeTrapMaxCPUThreshold.setStatus(_A)
hpeTrapMinCPUThreshold=NotificationType((1,3,6,1,4,1,11,5,7,5,8,1,4130,3,2))
hpeTrapMinCPUThreshold.setObjects(*((_B,_G),(_B,_D)))
if mibBuilder.loadTexts:hpeTrapMinCPUThreshold.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpeSynergyCpuUtilMIBObjects':hpeSynergyCpuUtilMIBObjects,'hpeCpuUtilMIB':hpeCpuUtilMIB,'hpeCpuUtilConfig':hpeCpuUtilConfig,_F:hpeSwitchMaxCPUThreshold,_G:hpeSwitchMinCPUThreshold,'hpeCpuUtiStatus':hpeCpuUtiStatus,_D:hpeSwitchAverageCPUUtilization,'hpeCpuUtilTraps':hpeCpuUtilTraps,'hpeTrapMaxCPUThreshold':hpeTrapMaxCPUThreshold,'hpeTrapMinCPUThreshold':hpeTrapMinCPUThreshold})