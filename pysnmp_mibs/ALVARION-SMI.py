_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alvarionWireless=ModuleIdentity((1,3,6,1,4,1,12394,1,10))
_AlvarionProducts_ObjectIdentity=ObjectIdentity
alvarionProducts=_AlvarionProducts_ObjectIdentity((1,3,6,1,4,1,12394,1,10,1))
if mibBuilder.loadTexts:alvarionProducts.setStatus(_A)
_AlvarionExperiment_ObjectIdentity=ObjectIdentity
alvarionExperiment=_AlvarionExperiment_ObjectIdentity((1,3,6,1,4,1,12394,1,10,3))
if mibBuilder.loadTexts:alvarionExperiment.setStatus(_A)
_AlvarionModules_ObjectIdentity=ObjectIdentity
alvarionModules=_AlvarionModules_ObjectIdentity((1,3,6,1,4,1,12394,1,10,4))
if mibBuilder.loadTexts:alvarionModules.setStatus(_A)
_AlvarionMgmtV2_ObjectIdentity=ObjectIdentity
alvarionMgmtV2=_AlvarionMgmtV2_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5))
if mibBuilder.loadTexts:alvarionMgmtV2.setStatus(_A)
_Variation_ObjectIdentity=ObjectIdentity
variation=_Variation_ObjectIdentity((1,3,6,1,4,1,12394,1,10,7))
if mibBuilder.loadTexts:variation.setStatus(_A)
mibBuilder.exportSymbols('ALVARION-SMI',**{'alvarionWireless':alvarionWireless,'alvarionProducts':alvarionProducts,'alvarionExperiment':alvarionExperiment,'alvarionModules':alvarionModules,'alvarionMgmtV2':alvarionMgmtV2,'variation':variation})