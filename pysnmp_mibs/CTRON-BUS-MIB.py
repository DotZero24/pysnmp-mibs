_G='read-only'
_F='unknown'
_E='DisplayString'
_D='Integer32'
_C='CtLaneDebugLevel'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctAtmfLanEmulation,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctAtmfLanEmulation')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class CtLaneDebugLevel(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('user',1),('all',2),('error',3),('warning',4),('informational',5),('detailed',6),('trace',7)))
_CtBus_ObjectIdentity=ObjectIdentity
ctBus=_CtBus_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,4))
_CtBusConfGroup_ObjectIdentity=ObjectIdentity
ctBusConfGroup=_CtBusConfGroup_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,4,1))
class _CtBusDSStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connected',1),('connectionLost',2),(_F,3)))
_CtBusDSStatus_Type.__name__=_D
_CtBusDSStatus_Object=MibScalar
ctBusDSStatus=_CtBusDSStatus_Object((1,3,6,1,4,1,52,4,3,5,4,1,1),_CtBusDSStatus_Type())
ctBusDSStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ctBusDSStatus.setStatus(_A)
class _CtBusUNIVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('uni30',2),('uni31',3),('uni40',4)))
_CtBusUNIVersion_Type.__name__=_D
_CtBusUNIVersion_Object=MibScalar
ctBusUNIVersion=_CtBusUNIVersion_Object((1,3,6,1,4,1,52,4,3,5,4,1,2),_CtBusUNIVersion_Type())
ctBusUNIVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:ctBusUNIVersion.setStatus(_A)
class _CtBusLaneDbgOutputFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtBusLaneDbgOutputFile_Type.__name__=_E
_CtBusLaneDbgOutputFile_Object=MibScalar
ctBusLaneDbgOutputFile=_CtBusLaneDbgOutputFile_Object((1,3,6,1,4,1,52,4,3,5,4,1,3),_CtBusLaneDbgOutputFile_Type())
ctBusLaneDbgOutputFile.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBusLaneDbgOutputFile.setStatus(_A)
class _CtBusLaneDbgConnectionServices_Type(CtLaneDebugLevel):defaultValue=1
_CtBusLaneDbgConnectionServices_Type.__name__=_C
_CtBusLaneDbgConnectionServices_Object=MibScalar
ctBusLaneDbgConnectionServices=_CtBusLaneDbgConnectionServices_Object((1,3,6,1,4,1,52,4,3,5,4,1,4),_CtBusLaneDbgConnectionServices_Type())
ctBusLaneDbgConnectionServices.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBusLaneDbgConnectionServices.setStatus(_A)
class _CtBusLaneDbgSNMP_Type(CtLaneDebugLevel):defaultValue=1
_CtBusLaneDbgSNMP_Type.__name__=_C
_CtBusLaneDbgSNMP_Object=MibScalar
ctBusLaneDbgSNMP=_CtBusLaneDbgSNMP_Object((1,3,6,1,4,1,52,4,3,5,4,1,5),_CtBusLaneDbgSNMP_Type())
ctBusLaneDbgSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBusLaneDbgSNMP.setStatus(_A)
class _CtBusLaneDbgBUS_Type(CtLaneDebugLevel):defaultValue=1
_CtBusLaneDbgBUS_Type.__name__=_C
_CtBusLaneDbgBUS_Object=MibScalar
ctBusLaneDbgBUS=_CtBusLaneDbgBUS_Object((1,3,6,1,4,1,52,4,3,5,4,1,6),_CtBusLaneDbgBUS_Type())
ctBusLaneDbgBUS.setMaxAccess(_B)
if mibBuilder.loadTexts:ctBusLaneDbgBUS.setStatus(_A)
mibBuilder.exportSymbols('CTRON-BUS-MIB',**{_C:CtLaneDebugLevel,'ctBus':ctBus,'ctBusConfGroup':ctBusConfGroup,'ctBusDSStatus':ctBusDSStatus,'ctBusUNIVersion':ctBusUNIVersion,'ctBusLaneDbgOutputFile':ctBusLaneDbgOutputFile,'ctBusLaneDbgConnectionServices':ctBusLaneDbgConnectionServices,'ctBusLaneDbgSNMP':ctBusLaneDbgSNMP,'ctBusLaneDbgBUS':ctBusLaneDbgBUS})