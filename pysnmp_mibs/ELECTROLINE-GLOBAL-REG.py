_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
electrolineGlobalRegModule=ModuleIdentity((1,3,6,1,4,1,5802,1,1,1,1))
if mibBuilder.loadTexts:electrolineGlobalRegModule.setRevisions(('1919-02-01 00:00',))
_ElectrolineCoRoot_ObjectIdentity=ObjectIdentity
electrolineCoRoot=_ElectrolineCoRoot_ObjectIdentity((1,3,6,1,4,1,5802))
if mibBuilder.loadTexts:electrolineCoRoot.setStatus(_A)
_ElectrolineRoot_ObjectIdentity=ObjectIdentity
electrolineRoot=_ElectrolineRoot_ObjectIdentity((1,3,6,1,4,1,5802,1))
if mibBuilder.loadTexts:electrolineRoot.setStatus(_A)
_ElectrolineReg_ObjectIdentity=ObjectIdentity
electrolineReg=_ElectrolineReg_ObjectIdentity((1,3,6,1,4,1,5802,1,1))
if mibBuilder.loadTexts:electrolineReg.setStatus(_A)
_ElectrolineModules_ObjectIdentity=ObjectIdentity
electrolineModules=_ElectrolineModules_ObjectIdentity((1,3,6,1,4,1,5802,1,1,1))
if mibBuilder.loadTexts:electrolineModules.setStatus(_A)
_ElectrolineHardwareProductsReg_ObjectIdentity=ObjectIdentity
electrolineHardwareProductsReg=_ElectrolineHardwareProductsReg_ObjectIdentity((1,3,6,1,4,1,5802,1,1,1,2))
if mibBuilder.loadTexts:electrolineHardwareProductsReg.setStatus(_A)
_ElectrolineSoftwareProductsReg_ObjectIdentity=ObjectIdentity
electrolineSoftwareProductsReg=_ElectrolineSoftwareProductsReg_ObjectIdentity((1,3,6,1,4,1,5802,1,1,1,3))
if mibBuilder.loadTexts:electrolineSoftwareProductsReg.setStatus(_A)
_ElectrolineGeneric_ObjectIdentity=ObjectIdentity
electrolineGeneric=_ElectrolineGeneric_ObjectIdentity((1,3,6,1,4,1,5802,1,2))
if mibBuilder.loadTexts:electrolineGeneric.setStatus(_A)
_ElectrolineProducts_ObjectIdentity=ObjectIdentity
electrolineProducts=_ElectrolineProducts_ObjectIdentity((1,3,6,1,4,1,5802,1,3))
if mibBuilder.loadTexts:electrolineProducts.setStatus(_A)
_ElectrolineHardwareProducts_ObjectIdentity=ObjectIdentity
electrolineHardwareProducts=_ElectrolineHardwareProducts_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1))
if mibBuilder.loadTexts:electrolineHardwareProducts.setStatus(_A)
_ElectrolineSoftwareProducts_ObjectIdentity=ObjectIdentity
electrolineSoftwareProducts=_ElectrolineSoftwareProducts_ObjectIdentity((1,3,6,1,4,1,5802,1,3,2))
if mibBuilder.loadTexts:electrolineSoftwareProducts.setStatus(_A)
_ElectrolineCaps_ObjectIdentity=ObjectIdentity
electrolineCaps=_ElectrolineCaps_ObjectIdentity((1,3,6,1,4,1,5802,1,4))
if mibBuilder.loadTexts:electrolineCaps.setStatus(_A)
_ElectrolineReqs_ObjectIdentity=ObjectIdentity
electrolineReqs=_ElectrolineReqs_ObjectIdentity((1,3,6,1,4,1,5802,1,5))
if mibBuilder.loadTexts:electrolineReqs.setStatus(_A)
_ElectrolineExpr_ObjectIdentity=ObjectIdentity
electrolineExpr=_ElectrolineExpr_ObjectIdentity((1,3,6,1,4,1,5802,1,6))
if mibBuilder.loadTexts:electrolineExpr.setStatus(_A)
_DmonMib_ObjectIdentity=ObjectIdentity
dmonMib=_DmonMib_ObjectIdentity((1,3,6,1,4,1,5802,999999))
mibBuilder.exportSymbols('ELECTROLINE-GLOBAL-REG',**{'electrolineCoRoot':electrolineCoRoot,'electrolineRoot':electrolineRoot,'electrolineReg':electrolineReg,'electrolineModules':electrolineModules,'electrolineGlobalRegModule':electrolineGlobalRegModule,'electrolineHardwareProductsReg':electrolineHardwareProductsReg,'electrolineSoftwareProductsReg':electrolineSoftwareProductsReg,'electrolineGeneric':electrolineGeneric,'electrolineProducts':electrolineProducts,'electrolineHardwareProducts':electrolineHardwareProducts,'electrolineSoftwareProducts':electrolineSoftwareProducts,'electrolineCaps':electrolineCaps,'electrolineReqs':electrolineReqs,'electrolineExpr':electrolineExpr,'dmonMib':dmonMib})