_G='syn100GhpeSwitchMinCPUThreshold'
_F='syn100GhpeSwitchMaxCPUThreshold'
_E='read-write'
_D='syn100GhpeSwitchAverageCPUUtilization'
_C='Integer32'
_B='SYNERGY100G-HPE-CPU-UTIL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpVCSE_100Gb_F32_Module,=mibBuilder.importSymbols('HPSVRMGMT-OID','hpVCSE-100Gb-F32-Module')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
syn100GhpeCpuUtilMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4130))
if mibBuilder.loadTexts:syn100GhpeCpuUtilMIB.setRevisions(('2019-12-19 00:00',))
_Syn100GhpeSynergyCpuUtilMIBObjects_ObjectIdentity=ObjectIdentity
syn100GhpeSynergyCpuUtilMIBObjects=_Syn100GhpeSynergyCpuUtilMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1))
_Syn100GhpeCpuUtilConfig_ObjectIdentity=ObjectIdentity
syn100GhpeCpuUtilConfig=_Syn100GhpeCpuUtilConfig_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4130,1))
class _Syn100GhpeSwitchMaxCPUThreshold_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Syn100GhpeSwitchMaxCPUThreshold_Type.__name__=_C
_Syn100GhpeSwitchMaxCPUThreshold_Object=MibScalar
syn100GhpeSwitchMaxCPUThreshold=_Syn100GhpeSwitchMaxCPUThreshold_Object((1,3,6,1,4,1,11,5,7,5,9,1,4130,1,1),_Syn100GhpeSwitchMaxCPUThreshold_Type())
syn100GhpeSwitchMaxCPUThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeSwitchMaxCPUThreshold.setStatus(_A)
class _Syn100GhpeSwitchMinCPUThreshold_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Syn100GhpeSwitchMinCPUThreshold_Type.__name__=_C
_Syn100GhpeSwitchMinCPUThreshold_Object=MibScalar
syn100GhpeSwitchMinCPUThreshold=_Syn100GhpeSwitchMinCPUThreshold_Object((1,3,6,1,4,1,11,5,7,5,9,1,4130,1,2),_Syn100GhpeSwitchMinCPUThreshold_Type())
syn100GhpeSwitchMinCPUThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeSwitchMinCPUThreshold.setStatus(_A)
_Syn100GhpeCpuUtiStatus_ObjectIdentity=ObjectIdentity
syn100GhpeCpuUtiStatus=_Syn100GhpeCpuUtiStatus_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4130,2))
_Syn100GhpeSwitchAverageCPUUtilization_Type=Integer32
_Syn100GhpeSwitchAverageCPUUtilization_Object=MibScalar
syn100GhpeSwitchAverageCPUUtilization=_Syn100GhpeSwitchAverageCPUUtilization_Object((1,3,6,1,4,1,11,5,7,5,9,1,4130,2,1),_Syn100GhpeSwitchAverageCPUUtilization_Type())
syn100GhpeSwitchAverageCPUUtilization.setMaxAccess('read-only')
if mibBuilder.loadTexts:syn100GhpeSwitchAverageCPUUtilization.setStatus(_A)
if mibBuilder.loadTexts:syn100GhpeSwitchAverageCPUUtilization.setUnits('percentage')
_Syn100GhpeCpuUtilTraps_ObjectIdentity=ObjectIdentity
syn100GhpeCpuUtilTraps=_Syn100GhpeCpuUtilTraps_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4130,3))
syn100GhpeTrapMaxCPUThreshold=NotificationType((1,3,6,1,4,1,11,5,7,5,9,1,4130,3,1))
syn100GhpeTrapMaxCPUThreshold.setObjects(*((_B,_F),(_B,_D)))
if mibBuilder.loadTexts:syn100GhpeTrapMaxCPUThreshold.setStatus(_A)
syn100GhpeTrapMinCPUThreshold=NotificationType((1,3,6,1,4,1,11,5,7,5,9,1,4130,3,2))
syn100GhpeTrapMinCPUThreshold.setObjects(*((_B,_G),(_B,_D)))
if mibBuilder.loadTexts:syn100GhpeTrapMinCPUThreshold.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'syn100GhpeSynergyCpuUtilMIBObjects':syn100GhpeSynergyCpuUtilMIBObjects,'syn100GhpeCpuUtilMIB':syn100GhpeCpuUtilMIB,'syn100GhpeCpuUtilConfig':syn100GhpeCpuUtilConfig,_F:syn100GhpeSwitchMaxCPUThreshold,_G:syn100GhpeSwitchMinCPUThreshold,'syn100GhpeCpuUtiStatus':syn100GhpeCpuUtiStatus,_D:syn100GhpeSwitchAverageCPUUtilization,'syn100GhpeCpuUtilTraps':syn100GhpeCpuUtilTraps,'syn100GhpeTrapMaxCPUThreshold':syn100GhpeTrapMaxCPUThreshold,'syn100GhpeTrapMinCPUThreshold':syn100GhpeTrapMinCPUThreshold})