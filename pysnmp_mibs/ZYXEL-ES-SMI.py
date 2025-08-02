_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
enterpriseSolution=ModuleIdentity((1,3,6,1,4,1,890,1,15))
_Zyxel_ObjectIdentity=ObjectIdentity
zyxel=_Zyxel_ObjectIdentity((1,3,6,1,4,1,890))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,890,1))
_EsAgentCapability_ObjectIdentity=ObjectIdentity
esAgentCapability=_EsAgentCapability_ObjectIdentity((1,3,6,1,4,1,890,1,15,1))
if mibBuilder.loadTexts:esAgentCapability.setStatus(_A)
_EsConformance_ObjectIdentity=ObjectIdentity
esConformance=_EsConformance_ObjectIdentity((1,3,6,1,4,1,890,1,15,2))
if mibBuilder.loadTexts:esConformance.setStatus(_A)
_EsMgmt_ObjectIdentity=ObjectIdentity
esMgmt=_EsMgmt_ObjectIdentity((1,3,6,1,4,1,890,1,15,3))
if mibBuilder.loadTexts:esMgmt.setStatus(_A)
_EsProductSpecific_ObjectIdentity=ObjectIdentity
esProductSpecific=_EsProductSpecific_ObjectIdentity((1,3,6,1,4,1,890,1,15,4))
if mibBuilder.loadTexts:esProductSpecific.setStatus(_A)
_Tenders_ObjectIdentity=ObjectIdentity
tenders=_Tenders_ObjectIdentity((1,3,6,1,4,1,890,1,15,4,4))
_ZyxelNAS_ObjectIdentity=ObjectIdentity
zyxelNAS=_ZyxelNAS_ObjectIdentity((1,3,6,1,4,1,890,1,15,4,4,5))
if mibBuilder.loadTexts:zyxelNAS.setStatus(_A)
_EsPartnerProducts_ObjectIdentity=ObjectIdentity
esPartnerProducts=_EsPartnerProducts_ObjectIdentity((1,3,6,1,4,1,890,1,15,5))
if mibBuilder.loadTexts:esPartnerProducts.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-ES-SMI',**{'zyxel':zyxel,'products':products,'enterpriseSolution':enterpriseSolution,'esAgentCapability':esAgentCapability,'esConformance':esConformance,'esMgmt':esMgmt,'esProductSpecific':esProductSpecific,'tenders':tenders,'zyxelNAS':zyxelNAS,'esPartnerProducts':esPartnerProducts})