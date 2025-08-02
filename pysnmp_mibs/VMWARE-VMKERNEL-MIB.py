if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwESX,=mibBuilder.importSymbols('VMWARE-PRODUCTS-MIB','vmwESX')
vmwProductSpecific,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwProductSpecific')
_EsxVMKernel_ObjectIdentity=ObjectIdentity
esxVMKernel=_EsxVMKernel_ObjectIdentity((1,3,6,1,4,1,6876,4,1,1))
_VmkLoaded_Type=DisplayString
_VmkLoaded_Object=MibScalar
vmkLoaded=_VmkLoaded_Object((1,3,6,1,4,1,6876,4,1,1,1),_VmkLoaded_Type())
vmkLoaded.setMaxAccess('read-only')
if mibBuilder.loadTexts:vmkLoaded.setStatus('mandatory')
mibBuilder.exportSymbols('VMWARE-VMKERNEL-MIB',**{'esxVMKernel':esxVMKernel,'vmkLoaded':vmkLoaded})