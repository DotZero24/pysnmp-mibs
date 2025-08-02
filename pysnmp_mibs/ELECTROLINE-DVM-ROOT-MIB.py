_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
electrolineHardwareProducts,=mibBuilder.importSymbols('ELECTROLINE-GLOBAL-REG','electrolineHardwareProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
electrolineDVM=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,3))
if mibBuilder.loadTexts:electrolineDVM.setRevisions(('2003-03-20 00:00',))
class ModulationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',-1),('qam16',0),('qam64',1),('qam256',2),('qam1024',3),('qam32',4),('qam128',5),('qpsk',6)))
_DvmInventory_ObjectIdentity=ObjectIdentity
dvmInventory=_DvmInventory_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,1))
if mibBuilder.loadTexts:dvmInventory.setStatus(_A)
_DvmConfiguration_ObjectIdentity=ObjectIdentity
dvmConfiguration=_DvmConfiguration_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,2))
if mibBuilder.loadTexts:dvmConfiguration.setStatus(_A)
_DvmStatus_ObjectIdentity=ObjectIdentity
dvmStatus=_DvmStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,3))
if mibBuilder.loadTexts:dvmStatus.setStatus(_A)
_DvmPrivate_ObjectIdentity=ObjectIdentity
dvmPrivate=_DvmPrivate_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4))
if mibBuilder.loadTexts:dvmPrivate.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-DVM-ROOT-MIB',**{'ModulationType':ModulationType,'electrolineDVM':electrolineDVM,'dvmInventory':dvmInventory,'dvmConfiguration':dvmConfiguration,'dvmStatus':dvmStatus,'dvmPrivate':dvmPrivate})