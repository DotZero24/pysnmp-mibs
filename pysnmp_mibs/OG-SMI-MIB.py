_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
opengear=ModuleIdentity((1,3,6,1,4,1,25049))
if mibBuilder.loadTexts:opengear.setRevisions(('2018-06-15 00:00','2013-11-15 00:00','2013-08-11 00:00','2010-03-22 11:27','2005-02-24 01:00'))
_OgProducts_ObjectIdentity=ObjectIdentity
ogProducts=_OgProducts_ObjectIdentity((1,3,6,1,4,1,25049,1))
if mibBuilder.loadTexts:ogProducts.setStatus(_A)
_OgLegacyMgmt_ObjectIdentity=ObjectIdentity
ogLegacyMgmt=_OgLegacyMgmt_ObjectIdentity((1,3,6,1,4,1,25049,2))
if mibBuilder.loadTexts:ogLegacyMgmt.setStatus(_A)
_OgExperimental_ObjectIdentity=ObjectIdentity
ogExperimental=_OgExperimental_ObjectIdentity((1,3,6,1,4,1,25049,3))
if mibBuilder.loadTexts:ogExperimental.setStatus(_A)
_OgInternal_ObjectIdentity=ObjectIdentity
ogInternal=_OgInternal_ObjectIdentity((1,3,6,1,4,1,25049,4))
if mibBuilder.loadTexts:ogInternal.setStatus(_A)
_OgReserved1_ObjectIdentity=ObjectIdentity
ogReserved1=_OgReserved1_ObjectIdentity((1,3,6,1,4,1,25049,5))
if mibBuilder.loadTexts:ogReserved1.setStatus(_A)
_OgReserved2_ObjectIdentity=ObjectIdentity
ogReserved2=_OgReserved2_ObjectIdentity((1,3,6,1,4,1,25049,6))
if mibBuilder.loadTexts:ogReserved2.setStatus(_A)
_OtherEnterprises_ObjectIdentity=ObjectIdentity
otherEnterprises=_OtherEnterprises_ObjectIdentity((1,3,6,1,4,1,25049,7))
if mibBuilder.loadTexts:otherEnterprises.setStatus(_A)
_OgAgentCapability_ObjectIdentity=ObjectIdentity
ogAgentCapability=_OgAgentCapability_ObjectIdentity((1,3,6,1,4,1,25049,8))
if mibBuilder.loadTexts:ogAgentCapability.setStatus(_A)
_OgConfig_ObjectIdentity=ObjectIdentity
ogConfig=_OgConfig_ObjectIdentity((1,3,6,1,4,1,25049,9))
if mibBuilder.loadTexts:ogConfig.setStatus(_A)
_OgMgmt_ObjectIdentity=ObjectIdentity
ogMgmt=_OgMgmt_ObjectIdentity((1,3,6,1,4,1,25049,10))
if mibBuilder.loadTexts:ogMgmt.setStatus(_A)
_OgModules_ObjectIdentity=ObjectIdentity
ogModules=_OgModules_ObjectIdentity((1,3,6,1,4,1,25049,11))
if mibBuilder.loadTexts:ogModules.setStatus(_A)
_OgSpecific_ObjectIdentity=ObjectIdentity
ogSpecific=_OgSpecific_ObjectIdentity((1,3,6,1,4,1,25049,18))
if mibBuilder.loadTexts:ogSpecific.setStatus(_A)
mibBuilder.exportSymbols('OG-SMI-MIB',**{'opengear':opengear,'ogProducts':ogProducts,'ogLegacyMgmt':ogLegacyMgmt,'ogExperimental':ogExperimental,'ogInternal':ogInternal,'ogReserved1':ogReserved1,'ogReserved2':ogReserved2,'otherEnterprises':otherEnterprises,'ogAgentCapability':ogAgentCapability,'ogConfig':ogConfig,'ogMgmt':ogMgmt,'ogModules':ogModules,'ogSpecific':ogSpecific})