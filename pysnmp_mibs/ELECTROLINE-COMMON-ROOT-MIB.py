_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
electrolineHardwareProducts,=mibBuilder.importSymbols('ELECTROLINE-GLOBAL-REG','electrolineHardwareProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
electrolineCommon=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,4))
if mibBuilder.loadTexts:electrolineCommon.setRevisions(('2014-01-14 00:00',))
_CommonInventory_ObjectIdentity=ObjectIdentity
commonInventory=_CommonInventory_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,1))
if mibBuilder.loadTexts:commonInventory.setStatus(_A)
_CommonConfiguration_ObjectIdentity=ObjectIdentity
commonConfiguration=_CommonConfiguration_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,2))
if mibBuilder.loadTexts:commonConfiguration.setStatus(_A)
_CommonStatus_ObjectIdentity=ObjectIdentity
commonStatus=_CommonStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,3))
if mibBuilder.loadTexts:commonStatus.setStatus(_A)
_CommonPrivate_ObjectIdentity=ObjectIdentity
commonPrivate=_CommonPrivate_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4))
if mibBuilder.loadTexts:commonPrivate.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-COMMON-ROOT-MIB',**{'electrolineCommon':electrolineCommon,'commonInventory':commonInventory,'commonConfiguration':commonConfiguration,'commonStatus':commonStatus,'commonPrivate':commonPrivate})