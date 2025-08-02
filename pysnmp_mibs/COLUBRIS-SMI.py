_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubris=ModuleIdentity((1,3,6,1,4,1,8744))
_ColubrisProducts_ObjectIdentity=ObjectIdentity
colubrisProducts=_ColubrisProducts_ObjectIdentity((1,3,6,1,4,1,8744,1))
if mibBuilder.loadTexts:colubrisProducts.setStatus(_A)
_ColubrisMgmt_ObjectIdentity=ObjectIdentity
colubrisMgmt=_ColubrisMgmt_ObjectIdentity((1,3,6,1,4,1,8744,2))
if mibBuilder.loadTexts:colubrisMgmt.setStatus('deprecated')
_ColubrisExperiment_ObjectIdentity=ObjectIdentity
colubrisExperiment=_ColubrisExperiment_ObjectIdentity((1,3,6,1,4,1,8744,3))
if mibBuilder.loadTexts:colubrisExperiment.setStatus(_A)
_ColubrisModules_ObjectIdentity=ObjectIdentity
colubrisModules=_ColubrisModules_ObjectIdentity((1,3,6,1,4,1,8744,4))
if mibBuilder.loadTexts:colubrisModules.setStatus(_A)
_ColubrisMgmtV2_ObjectIdentity=ObjectIdentity
colubrisMgmtV2=_ColubrisMgmtV2_ObjectIdentity((1,3,6,1,4,1,8744,5))
if mibBuilder.loadTexts:colubrisMgmtV2.setStatus(_A)
_Extensions_ObjectIdentity=ObjectIdentity
extensions=_Extensions_ObjectIdentity((1,3,6,1,4,1,8744,6))
if mibBuilder.loadTexts:extensions.setStatus(_A)
_Variation_ObjectIdentity=ObjectIdentity
variation=_Variation_ObjectIdentity((1,3,6,1,4,1,8744,7))
if mibBuilder.loadTexts:variation.setStatus(_A)
mibBuilder.exportSymbols('COLUBRIS-SMI',**{'colubris':colubris,'colubrisProducts':colubrisProducts,'colubrisMgmt':colubrisMgmt,'colubrisExperiment':colubrisExperiment,'colubrisModules':colubrisModules,'colubrisMgmtV2':colubrisMgmtV2,'extensions':extensions,'variation':variation})