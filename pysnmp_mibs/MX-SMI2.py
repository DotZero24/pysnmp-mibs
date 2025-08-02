_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrix,=mibBuilder.importSymbols('MX-SMI','mediatrix')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_MediatrixSystem_ObjectIdentity=ObjectIdentity
mediatrixSystem=_MediatrixSystem_ObjectIdentity((1,3,6,1,4,1,4935,1000))
if mibBuilder.loadTexts:mediatrixSystem.setStatus(_A)
_Gen5_ObjectIdentity=ObjectIdentity
gen5=_Gen5_ObjectIdentity((1,3,6,1,4,1,4935,1000,100))
if mibBuilder.loadTexts:gen5.setStatus(_A)
_MediatrixProducts_ObjectIdentity=ObjectIdentity
mediatrixProducts=_MediatrixProducts_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,100))
if mibBuilder.loadTexts:mediatrixProducts.setStatus(_A)
_MediatrixCommon_ObjectIdentity=ObjectIdentity
mediatrixCommon=_MediatrixCommon_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200))
if mibBuilder.loadTexts:mediatrixCommon.setStatus(_A)
_MediatrixServices_ObjectIdentity=ObjectIdentity
mediatrixServices=_MediatrixServices_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100))
if mibBuilder.loadTexts:mediatrixServices.setStatus(_A)
_MediatrixHardware_ObjectIdentity=ObjectIdentity
mediatrixHardware=_MediatrixHardware_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,500))
if mibBuilder.loadTexts:mediatrixHardware.setStatus(_A)
mibBuilder.exportSymbols('MX-SMI2',**{'mediatrixSystem':mediatrixSystem,'gen5':gen5,'mediatrixProducts':mediatrixProducts,'mediatrixCommon':mediatrixCommon,'mediatrixServices':mediatrixServices,'mediatrixHardware':mediatrixHardware})