_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alliedTelesis=ModuleIdentity((1,3,6,1,4,1,207))
if mibBuilder.loadTexts:alliedTelesis.setRevisions(('2006-06-14 00:00','2008-02-28 00:00','2010-06-15 00:15'))
class DisplayStringUnsized(TextualConvention,OctetString):status=_A;displayHint='255a'
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,207,1))
if mibBuilder.loadTexts:products.setStatus(_A)
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
if mibBuilder.loadTexts:mibObject.setStatus(_A)
_BrouterMib_ObjectIdentity=ObjectIdentity
brouterMib=_BrouterMib_ObjectIdentity((1,3,6,1,4,1,207,8,4))
if mibBuilder.loadTexts:brouterMib.setStatus(_A)
_AtRouter_ObjectIdentity=ObjectIdentity
atRouter=_AtRouter_ObjectIdentity((1,3,6,1,4,1,207,8,4,4))
if mibBuilder.loadTexts:atRouter.setStatus(_A)
_Objects_ObjectIdentity=ObjectIdentity
objects=_Objects_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,1))
if mibBuilder.loadTexts:objects.setStatus(_A)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,2))
if mibBuilder.loadTexts:traps.setStatus(_A)
_Sysinfo_ObjectIdentity=ObjectIdentity
sysinfo=_Sysinfo_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3))
if mibBuilder.loadTexts:sysinfo.setStatus(_A)
_Modules_ObjectIdentity=ObjectIdentity
modules=_Modules_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4))
if mibBuilder.loadTexts:modules.setStatus(_A)
_ArInterfaces_ObjectIdentity=ObjectIdentity
arInterfaces=_ArInterfaces_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,5))
if mibBuilder.loadTexts:arInterfaces.setStatus(_A)
_Protocols_ObjectIdentity=ObjectIdentity
protocols=_Protocols_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,6))
if mibBuilder.loadTexts:protocols.setStatus(_A)
_AtAgents_ObjectIdentity=ObjectIdentity
atAgents=_AtAgents_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,7))
if mibBuilder.loadTexts:atAgents.setStatus(_A)
mibBuilder.exportSymbols('AT-SMI-MIB',**{'DisplayStringUnsized':DisplayStringUnsized,'alliedTelesis':alliedTelesis,'products':products,'mibObject':mibObject,'brouterMib':brouterMib,'atRouter':atRouter,'objects':objects,'traps':traps,'sysinfo':sysinfo,'modules':modules,'arInterfaces':arInterfaces,'protocols':protocols,'atAgents':atAgents})