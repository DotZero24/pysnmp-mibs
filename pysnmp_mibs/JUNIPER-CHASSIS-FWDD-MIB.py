_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxFwdd=ModuleIdentity((1,3,6,1,4,1,2636,3,34))
_JnxFwddProcess_ObjectIdentity=ObjectIdentity
jnxFwddProcess=_JnxFwddProcess_ObjectIdentity((1,3,6,1,4,1,2636,3,34,1))
_JnxFwddMicroKernelCPUUsage_Type=Gauge32
_JnxFwddMicroKernelCPUUsage_Object=MibScalar
jnxFwddMicroKernelCPUUsage=_JnxFwddMicroKernelCPUUsage_Object((1,3,6,1,4,1,2636,3,34,1,1),_JnxFwddMicroKernelCPUUsage_Type())
jnxFwddMicroKernelCPUUsage.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxFwddMicroKernelCPUUsage.setStatus(_B)
_JnxFwddRtThreadsCPUUsage_Type=Gauge32
_JnxFwddRtThreadsCPUUsage_Object=MibScalar
jnxFwddRtThreadsCPUUsage=_JnxFwddRtThreadsCPUUsage_Object((1,3,6,1,4,1,2636,3,34,1,2),_JnxFwddRtThreadsCPUUsage_Type())
jnxFwddRtThreadsCPUUsage.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxFwddRtThreadsCPUUsage.setStatus(_B)
_JnxFwddHeapUsage_Type=Gauge32
_JnxFwddHeapUsage_Object=MibScalar
jnxFwddHeapUsage=_JnxFwddHeapUsage_Object((1,3,6,1,4,1,2636,3,34,1,3),_JnxFwddHeapUsage_Type())
jnxFwddHeapUsage.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxFwddHeapUsage.setStatus(_B)
_JnxFwddDmaMemUsage_Type=Gauge32
_JnxFwddDmaMemUsage_Object=MibScalar
jnxFwddDmaMemUsage=_JnxFwddDmaMemUsage_Object((1,3,6,1,4,1,2636,3,34,1,4),_JnxFwddDmaMemUsage_Type())
jnxFwddDmaMemUsage.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxFwddDmaMemUsage.setStatus(_B)
_JnxFwddUpTime_Type=Integer32
_JnxFwddUpTime_Object=MibScalar
jnxFwddUpTime=_JnxFwddUpTime_Object((1,3,6,1,4,1,2636,3,34,1,5),_JnxFwddUpTime_Type())
jnxFwddUpTime.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxFwddUpTime.setStatus(_B)
if mibBuilder.loadTexts:jnxFwddUpTime.setUnits('seconds')
mibBuilder.exportSymbols('JUNIPER-CHASSIS-FWDD-MIB',**{'jnxFwdd':jnxFwdd,'jnxFwddProcess':jnxFwddProcess,'jnxFwddMicroKernelCPUUsage':jnxFwddMicroKernelCPUUsage,'jnxFwddRtThreadsCPUUsage':jnxFwddRtThreadsCPUUsage,'jnxFwddHeapUsage':jnxFwddHeapUsage,'jnxFwddDmaMemUsage':jnxFwddDmaMemUsage,'jnxFwddUpTime':jnxFwddUpTime})