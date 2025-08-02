_C='mandatory'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm6611_ObjectIdentity=ObjectIdentity
ibm6611=_Ibm6611_ObjectIdentity((1,3,6,1,4,1,2,6,2))
_Ibmappn_ObjectIdentity=ObjectIdentity
ibmappn=_Ibmappn_ObjectIdentity((1,3,6,1,4,1,2,6,2,13))
_IbmappnNode_ObjectIdentity=ObjectIdentity
ibmappnNode=_IbmappnNode_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1))
_IbmappnMemoryUse_ObjectIdentity=ObjectIdentity
ibmappnMemoryUse=_IbmappnMemoryUse_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,7))
class _IbmappnMemorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IbmappnMemorySize_Type.__name__=_A
_IbmappnMemorySize_Object=MibScalar
ibmappnMemorySize=_IbmappnMemorySize_Object((1,3,6,1,4,1,2,6,2,13,1,7,1),_IbmappnMemorySize_Type())
ibmappnMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemorySize.setStatus(_C)
class _IbmappnMemoryUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IbmappnMemoryUsed_Type.__name__=_A
_IbmappnMemoryUsed_Object=MibScalar
ibmappnMemoryUsed=_IbmappnMemoryUsed_Object((1,3,6,1,4,1,2,6,2,13,1,7,2),_IbmappnMemoryUsed_Type())
ibmappnMemoryUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemoryUsed.setStatus(_C)
class _IbmappnMemoryWarnThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IbmappnMemoryWarnThresh_Type.__name__=_A
_IbmappnMemoryWarnThresh_Object=MibScalar
ibmappnMemoryWarnThresh=_IbmappnMemoryWarnThresh_Object((1,3,6,1,4,1,2,6,2,13,1,7,3),_IbmappnMemoryWarnThresh_Type())
ibmappnMemoryWarnThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemoryWarnThresh.setStatus(_C)
class _IbmappnMemoryCritThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IbmappnMemoryCritThresh_Type.__name__=_A
_IbmappnMemoryCritThresh_Object=MibScalar
ibmappnMemoryCritThresh=_IbmappnMemoryCritThresh_Object((1,3,6,1,4,1,2,6,2,13,1,7,4),_IbmappnMemoryCritThresh_Type())
ibmappnMemoryCritThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemoryCritThresh.setStatus(_C)
mibBuilder.exportSymbols('IBMAPPNMEMORY-MIB',**{'ibm':ibm,'ibmProd':ibmProd,'ibm6611':ibm6611,'ibmappn':ibmappn,'ibmappnNode':ibmappnNode,'ibmappnMemoryUse':ibmappnMemoryUse,'ibmappnMemorySize':ibmappnMemorySize,'ibmappnMemoryUsed':ibmappnMemoryUsed,'ibmappnMemoryWarnThresh':ibmappnMemoryWarnThresh,'ibmappnMemoryCritThresh':ibmappnMemoryCritThresh})