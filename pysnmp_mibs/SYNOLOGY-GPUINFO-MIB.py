_J='gpuInfoGroup'
_I='gpuMemoryTotal'
_H='gpuMemoryUsed'
_G='gpuMemoryFree'
_F='gpuMemoryUtilization'
_E='gpuUtilization'
_D='gpuInfoSupported'
_C='read-only'
_B='SYNOLOGY-GPUINFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gpuInfo=ModuleIdentity((1,3,6,1,4,1,6574,108))
if mibBuilder.loadTexts:gpuInfo.setRevisions(('2018-12-03 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_GpuInfoSupported_Type=Integer32
_GpuInfoSupported_Object=MibScalar
gpuInfoSupported=_GpuInfoSupported_Object((1,3,6,1,4,1,6574,108,1),_GpuInfoSupported_Type())
gpuInfoSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:gpuInfoSupported.setStatus(_A)
_GpuUtilization_Type=Integer32
_GpuUtilization_Object=MibScalar
gpuUtilization=_GpuUtilization_Object((1,3,6,1,4,1,6574,108,2),_GpuUtilization_Type())
gpuUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:gpuUtilization.setStatus(_A)
_GpuMemoryUtilization_Type=Integer32
_GpuMemoryUtilization_Object=MibScalar
gpuMemoryUtilization=_GpuMemoryUtilization_Object((1,3,6,1,4,1,6574,108,3),_GpuMemoryUtilization_Type())
gpuMemoryUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:gpuMemoryUtilization.setStatus(_A)
_GpuMemoryFree_Type=Integer32
_GpuMemoryFree_Object=MibScalar
gpuMemoryFree=_GpuMemoryFree_Object((1,3,6,1,4,1,6574,108,4),_GpuMemoryFree_Type())
gpuMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:gpuMemoryFree.setStatus(_A)
_GpuMemoryUsed_Type=Integer32
_GpuMemoryUsed_Object=MibScalar
gpuMemoryUsed=_GpuMemoryUsed_Object((1,3,6,1,4,1,6574,108,5),_GpuMemoryUsed_Type())
gpuMemoryUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:gpuMemoryUsed.setStatus(_A)
_GpuMemoryTotal_Type=Integer32
_GpuMemoryTotal_Object=MibScalar
gpuMemoryTotal=_GpuMemoryTotal_Object((1,3,6,1,4,1,6574,108,6),_GpuMemoryTotal_Type())
gpuMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:gpuMemoryTotal.setStatus(_A)
_GpuInfoConformance_ObjectIdentity=ObjectIdentity
gpuInfoConformance=_GpuInfoConformance_ObjectIdentity((1,3,6,1,4,1,6574,108,7))
_GpuInfoCompliances_ObjectIdentity=ObjectIdentity
gpuInfoCompliances=_GpuInfoCompliances_ObjectIdentity((1,3,6,1,4,1,6574,108,7,1))
_GpuInfoGroups_ObjectIdentity=ObjectIdentity
gpuInfoGroups=_GpuInfoGroups_ObjectIdentity((1,3,6,1,4,1,6574,108,7,2))
gpuInfoGroup=ObjectGroup((1,3,6,1,4,1,6574,108,7,2,1))
gpuInfoGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:gpuInfoGroup.setStatus(_A)
gpuInfoCompliance=ModuleCompliance((1,3,6,1,4,1,6574,108,7,1,1))
gpuInfoCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:gpuInfoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'gpuInfo':gpuInfo,_D:gpuInfoSupported,_E:gpuUtilization,_F:gpuMemoryUtilization,_G:gpuMemoryFree,_H:gpuMemoryUsed,_I:gpuMemoryTotal,'gpuInfoConformance':gpuInfoConformance,'gpuInfoCompliances':gpuInfoCompliances,'gpuInfoCompliance':gpuInfoCompliance,'gpuInfoGroups':gpuInfoGroups,_J:gpuInfoGroup})