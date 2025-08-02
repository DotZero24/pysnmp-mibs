_E='ibmMainProcessorLoadIndex'
_D='IBMCPU-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm6611_ObjectIdentity=ObjectIdentity
ibm6611=_Ibm6611_ObjectIdentity((1,3,6,1,4,1,2,6,2))
_Ibmsystem_ObjectIdentity=ObjectIdentity
ibmsystem=_Ibmsystem_ObjectIdentity((1,3,6,1,4,1,2,6,2,4))
_IbmMainProcessorLoadTable_Object=MibTable
ibmMainProcessorLoadTable=_IbmMainProcessorLoadTable_Object((1,3,6,1,4,1,2,6,2,4,1))
if mibBuilder.loadTexts:ibmMainProcessorLoadTable.setStatus(_A)
_IbmMainProcessorLoadEntry_Object=MibTableRow
ibmMainProcessorLoadEntry=_IbmMainProcessorLoadEntry_Object((1,3,6,1,4,1,2,6,2,4,1,1))
ibmMainProcessorLoadEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibmMainProcessorLoadEntry.setStatus(_A)
class _IbmMainProcessorLoadIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_IbmMainProcessorLoadIndex_Type.__name__=_C
_IbmMainProcessorLoadIndex_Object=MibTableColumn
ibmMainProcessorLoadIndex=_IbmMainProcessorLoadIndex_Object((1,3,6,1,4,1,2,6,2,4,1,1,1),_IbmMainProcessorLoadIndex_Type())
ibmMainProcessorLoadIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmMainProcessorLoadIndex.setStatus(_A)
_IbmMainProcessorLoad_Type=Gauge32
_IbmMainProcessorLoad_Object=MibTableColumn
ibmMainProcessorLoad=_IbmMainProcessorLoad_Object((1,3,6,1,4,1,2,6,2,4,1,1,2),_IbmMainProcessorLoad_Type())
ibmMainProcessorLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmMainProcessorLoad.setStatus(_A)
_NetView6000SubAgent_ObjectIdentity=ObjectIdentity
netView6000SubAgent=_NetView6000SubAgent_ObjectIdentity((1,3,6,1,4,1,2,6,4))
_Nv6saComputerSystem_ObjectIdentity=ObjectIdentity
nv6saComputerSystem=_Nv6saComputerSystem_ObjectIdentity((1,3,6,1,4,1,2,6,4,5))
_Nv6saComputerSystemLoad_Type=Gauge32
_Nv6saComputerSystemLoad_Object=MibScalar
nv6saComputerSystemLoad=_Nv6saComputerSystemLoad_Object((1,3,6,1,4,1,2,6,4,5,1),_Nv6saComputerSystemLoad_Type())
nv6saComputerSystemLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:nv6saComputerSystemLoad.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ibm':ibm,'ibmProd':ibmProd,'ibm6611':ibm6611,'ibmsystem':ibmsystem,'ibmMainProcessorLoadTable':ibmMainProcessorLoadTable,'ibmMainProcessorLoadEntry':ibmMainProcessorLoadEntry,_E:ibmMainProcessorLoadIndex,'ibmMainProcessorLoad':ibmMainProcessorLoad,'netView6000SubAgent':netView6000SubAgent,'nv6saComputerSystem':nv6saComputerSystem,'nv6saComputerSystemLoad':nv6saComputerSystemLoad})