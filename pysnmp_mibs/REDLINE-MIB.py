_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
redline=ModuleIdentity((1,3,6,1,4,1,10728))
if mibBuilder.loadTexts:redline.setRevisions(('2005-06-08 17:50','2001-11-08 00:00','2001-08-12 00:00','2002-03-13 00:00'))
_RedlineProducts_ObjectIdentity=ObjectIdentity
redlineProducts=_RedlineProducts_ObjectIdentity((1,3,6,1,4,1,10728,1))
if mibBuilder.loadTexts:redlineProducts.setStatus(_A)
_RedlineMgmt_ObjectIdentity=ObjectIdentity
redlineMgmt=_RedlineMgmt_ObjectIdentity((1,3,6,1,4,1,10728,2))
if mibBuilder.loadTexts:redlineMgmt.setStatus(_A)
_RedlineSystem_ObjectIdentity=ObjectIdentity
redlineSystem=_RedlineSystem_ObjectIdentity((1,3,6,1,4,1,10728,2,1))
_RedlineTransmission_ObjectIdentity=ObjectIdentity
redlineTransmission=_RedlineTransmission_ObjectIdentity((1,3,6,1,4,1,10728,2,10))
_RedlineExperiment_ObjectIdentity=ObjectIdentity
redlineExperiment=_RedlineExperiment_ObjectIdentity((1,3,6,1,4,1,10728,3))
if mibBuilder.loadTexts:redlineExperiment.setStatus(_A)
_RedlineAdmin_ObjectIdentity=ObjectIdentity
redlineAdmin=_RedlineAdmin_ObjectIdentity((1,3,6,1,4,1,10728,4))
if mibBuilder.loadTexts:redlineAdmin.setStatus(_A)
_RedlineModules_ObjectIdentity=ObjectIdentity
redlineModules=_RedlineModules_ObjectIdentity((1,3,6,1,4,1,10728,5))
if mibBuilder.loadTexts:redlineModules.setStatus(_A)
_RedlinePartners_ObjectIdentity=ObjectIdentity
redlinePartners=_RedlinePartners_ObjectIdentity((1,3,6,1,4,1,10728,6))
if mibBuilder.loadTexts:redlinePartners.setStatus(_A)
_RedlineOtherEnterpises_ObjectIdentity=ObjectIdentity
redlineOtherEnterpises=_RedlineOtherEnterpises_ObjectIdentity((1,3,6,1,4,1,10728,7))
if mibBuilder.loadTexts:redlineOtherEnterpises.setStatus(_A)
_RedlineAgentCapability_ObjectIdentity=ObjectIdentity
redlineAgentCapability=_RedlineAgentCapability_ObjectIdentity((1,3,6,1,4,1,10728,8))
if mibBuilder.loadTexts:redlineAgentCapability.setStatus(_A)
mibBuilder.exportSymbols('REDLINE-MIB',**{'redline':redline,'redlineProducts':redlineProducts,'redlineMgmt':redlineMgmt,'redlineSystem':redlineSystem,'redlineTransmission':redlineTransmission,'redlineExperiment':redlineExperiment,'redlineAdmin':redlineAdmin,'redlineModules':redlineModules,'redlinePartners':redlinePartners,'redlineOtherEnterpises':redlineOtherEnterpises,'redlineAgentCapability':redlineAgentCapability})