_B='2007-11-17 10:00'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxWxGlobalRegModule=ModuleIdentity((1,3,6,1,4,1,8239,1,1,1))
if mibBuilder.loadTexts:jnxWxGlobalRegModule.setRevisions((_B,_B,'2007-11-14 01:30','2006-06-08 18:00','2005-05-09 10:12','2004-03-15 14:00','2003-06-26 20:00','2001-07-29 22:00'))
_JuniperWxRoot_ObjectIdentity=ObjectIdentity
juniperWxRoot=_JuniperWxRoot_ObjectIdentity((1,3,6,1,4,1,8239))
if mibBuilder.loadTexts:juniperWxRoot.setStatus(_A)
_JnxWxReg_ObjectIdentity=ObjectIdentity
jnxWxReg=_JnxWxReg_ObjectIdentity((1,3,6,1,4,1,8239,1))
if mibBuilder.loadTexts:jnxWxReg.setStatus(_A)
_JnxWxModules_ObjectIdentity=ObjectIdentity
jnxWxModules=_JnxWxModules_ObjectIdentity((1,3,6,1,4,1,8239,1,1))
if mibBuilder.loadTexts:jnxWxModules.setStatus(_A)
_JnxWxProduct_ObjectIdentity=ObjectIdentity
jnxWxProduct=_JnxWxProduct_ObjectIdentity((1,3,6,1,4,1,8239,1,2))
if mibBuilder.loadTexts:jnxWxProduct.setStatus(_A)
_JnxWxProductWx50_ObjectIdentity=ObjectIdentity
jnxWxProductWx50=_JnxWxProductWx50_ObjectIdentity((1,3,6,1,4,1,8239,1,2,1))
if mibBuilder.loadTexts:jnxWxProductWx50.setStatus(_A)
_JnxWxProductWx55_ObjectIdentity=ObjectIdentity
jnxWxProductWx55=_JnxWxProductWx55_ObjectIdentity((1,3,6,1,4,1,8239,1,2,2))
if mibBuilder.loadTexts:jnxWxProductWx55.setStatus(_A)
_JnxWxProductWx20_ObjectIdentity=ObjectIdentity
jnxWxProductWx20=_JnxWxProductWx20_ObjectIdentity((1,3,6,1,4,1,8239,1,2,3))
if mibBuilder.loadTexts:jnxWxProductWx20.setStatus(_A)
_JnxWxProductWx80_ObjectIdentity=ObjectIdentity
jnxWxProductWx80=_JnxWxProductWx80_ObjectIdentity((1,3,6,1,4,1,8239,1,2,4))
if mibBuilder.loadTexts:jnxWxProductWx80.setStatus(_A)
_JnxWxProductWx100_ObjectIdentity=ObjectIdentity
jnxWxProductWx100=_JnxWxProductWx100_ObjectIdentity((1,3,6,1,4,1,8239,1,2,5))
if mibBuilder.loadTexts:jnxWxProductWx100.setStatus(_A)
_JnxWxProductWxc500_ObjectIdentity=ObjectIdentity
jnxWxProductWxc500=_JnxWxProductWxc500_ObjectIdentity((1,3,6,1,4,1,8239,1,2,6))
if mibBuilder.loadTexts:jnxWxProductWxc500.setStatus(_A)
_JnxWxProductWx15_ObjectIdentity=ObjectIdentity
jnxWxProductWx15=_JnxWxProductWx15_ObjectIdentity((1,3,6,1,4,1,8239,1,2,7))
if mibBuilder.loadTexts:jnxWxProductWx15.setStatus(_A)
_JnxWxProductWxc250_ObjectIdentity=ObjectIdentity
jnxWxProductWxc250=_JnxWxProductWxc250_ObjectIdentity((1,3,6,1,4,1,8239,1,2,8))
if mibBuilder.loadTexts:jnxWxProductWxc250.setStatus(_A)
_JnxWxProductWx60_ObjectIdentity=ObjectIdentity
jnxWxProductWx60=_JnxWxProductWx60_ObjectIdentity((1,3,6,1,4,1,8239,1,2,9))
if mibBuilder.loadTexts:jnxWxProductWx60.setStatus(_A)
_JnxWxProductWxc590_ObjectIdentity=ObjectIdentity
jnxWxProductWxc590=_JnxWxProductWxc590_ObjectIdentity((1,3,6,1,4,1,8239,1,2,10))
if mibBuilder.loadTexts:jnxWxProductWxc590.setStatus(_A)
_JnxWxProductIsm200Wxc_ObjectIdentity=ObjectIdentity
jnxWxProductIsm200Wxc=_JnxWxProductIsm200Wxc_ObjectIdentity((1,3,6,1,4,1,8239,1,2,11))
if mibBuilder.loadTexts:jnxWxProductIsm200Wxc.setStatus(_A)
_JnxWxProductWxc1800_ObjectIdentity=ObjectIdentity
jnxWxProductWxc1800=_JnxWxProductWxc1800_ObjectIdentity((1,3,6,1,4,1,8239,1,2,12))
if mibBuilder.loadTexts:jnxWxProductWxc1800.setStatus(_A)
_JnxWxProductWxc2600_ObjectIdentity=ObjectIdentity
jnxWxProductWxc2600=_JnxWxProductWxc2600_ObjectIdentity((1,3,6,1,4,1,8239,1,2,13))
if mibBuilder.loadTexts:jnxWxProductWxc2600.setStatus(_A)
_JnxWxProductWxc3400_ObjectIdentity=ObjectIdentity
jnxWxProductWxc3400=_JnxWxProductWxc3400_ObjectIdentity((1,3,6,1,4,1,8239,1,2,14))
if mibBuilder.loadTexts:jnxWxProductWxc3400.setStatus(_A)
_JnxWxMibs_ObjectIdentity=ObjectIdentity
jnxWxMibs=_JnxWxMibs_ObjectIdentity((1,3,6,1,4,1,8239,2))
if mibBuilder.loadTexts:jnxWxMibs.setStatus(_A)
_JnxWxCommonMib_ObjectIdentity=ObjectIdentity
jnxWxCommonMib=_JnxWxCommonMib_ObjectIdentity((1,3,6,1,4,1,8239,2,1))
if mibBuilder.loadTexts:jnxWxCommonMib.setStatus(_A)
_JnxWxSpecificMib_ObjectIdentity=ObjectIdentity
jnxWxSpecificMib=_JnxWxSpecificMib_ObjectIdentity((1,3,6,1,4,1,8239,2,2))
if mibBuilder.loadTexts:jnxWxSpecificMib.setStatus(_A)
_JnxWxCaps_ObjectIdentity=ObjectIdentity
jnxWxCaps=_JnxWxCaps_ObjectIdentity((1,3,6,1,4,1,8239,3))
if mibBuilder.loadTexts:jnxWxCaps.setStatus(_A)
_JnxWxReqs_ObjectIdentity=ObjectIdentity
jnxWxReqs=_JnxWxReqs_ObjectIdentity((1,3,6,1,4,1,8239,4))
if mibBuilder.loadTexts:jnxWxReqs.setStatus(_A)
_JnxWxExpr_ObjectIdentity=ObjectIdentity
jnxWxExpr=_JnxWxExpr_ObjectIdentity((1,3,6,1,4,1,8239,5))
if mibBuilder.loadTexts:jnxWxExpr.setStatus(_A)
mibBuilder.exportSymbols('JUNIPER-WX-GLOBAL-REG',**{'juniperWxRoot':juniperWxRoot,'jnxWxReg':jnxWxReg,'jnxWxModules':jnxWxModules,'jnxWxGlobalRegModule':jnxWxGlobalRegModule,'jnxWxProduct':jnxWxProduct,'jnxWxProductWx50':jnxWxProductWx50,'jnxWxProductWx55':jnxWxProductWx55,'jnxWxProductWx20':jnxWxProductWx20,'jnxWxProductWx80':jnxWxProductWx80,'jnxWxProductWx100':jnxWxProductWx100,'jnxWxProductWxc500':jnxWxProductWxc500,'jnxWxProductWx15':jnxWxProductWx15,'jnxWxProductWxc250':jnxWxProductWxc250,'jnxWxProductWx60':jnxWxProductWx60,'jnxWxProductWxc590':jnxWxProductWxc590,'jnxWxProductIsm200Wxc':jnxWxProductIsm200Wxc,'jnxWxProductWxc1800':jnxWxProductWxc1800,'jnxWxProductWxc2600':jnxWxProductWxc2600,'jnxWxProductWxc3400':jnxWxProductWxc3400,'jnxWxMibs':jnxWxMibs,'jnxWxCommonMib':jnxWxCommonMib,'jnxWxSpecificMib':jnxWxSpecificMib,'jnxWxCaps':jnxWxCaps,'jnxWxReqs':jnxWxReqs,'jnxWxExpr':jnxWxExpr})