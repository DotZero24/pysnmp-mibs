_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tippingpoint=ModuleIdentity((1,3,6,1,4,1,10734))
if mibBuilder.loadTexts:tippingpoint.setRevisions(('2016-05-25 18:54',))
_Tpt_reg_ObjectIdentity=ObjectIdentity
tpt_reg=_Tpt_reg_ObjectIdentity((1,3,6,1,4,1,10734,1))
if mibBuilder.loadTexts:tpt_reg.setStatus(_A)
_Tpt_generic_ObjectIdentity=ObjectIdentity
tpt_generic=_Tpt_generic_ObjectIdentity((1,3,6,1,4,1,10734,2))
if mibBuilder.loadTexts:tpt_generic.setStatus(_A)
_Tpt_products_ObjectIdentity=ObjectIdentity
tpt_products=_Tpt_products_ObjectIdentity((1,3,6,1,4,1,10734,3))
if mibBuilder.loadTexts:tpt_products.setStatus(_A)
_Tpt_caps_ObjectIdentity=ObjectIdentity
tpt_caps=_Tpt_caps_ObjectIdentity((1,3,6,1,4,1,10734,4))
if mibBuilder.loadTexts:tpt_caps.setStatus(_A)
_Tpt_reqs_ObjectIdentity=ObjectIdentity
tpt_reqs=_Tpt_reqs_ObjectIdentity((1,3,6,1,4,1,10734,5))
if mibBuilder.loadTexts:tpt_reqs.setStatus(_A)
_Tpt_expr_ObjectIdentity=ObjectIdentity
tpt_expr=_Tpt_expr_ObjectIdentity((1,3,6,1,4,1,10734,6))
if mibBuilder.loadTexts:tpt_expr.setStatus(_A)
mibBuilder.exportSymbols('TIPPINGPOINT-REG-MIB',**{'tippingpoint':tippingpoint,'tpt-reg':tpt_reg,'tpt-generic':tpt_generic,'tpt-products':tpt_products,'tpt-caps':tpt_caps,'tpt-reqs':tpt_reqs,'tpt-expr':tpt_expr})